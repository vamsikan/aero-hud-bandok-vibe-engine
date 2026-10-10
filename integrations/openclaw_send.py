"""Pull a caption from the AERO·HUD API and deliver it through OpenClaw.

The app only generates text; OpenClaw owns the channel session (WhatsApp,
Telegram, Signal, ...). Running this where OpenClaw is paired means the hosted
app never needs inbound access or a gateway token.

    python3 -m integrations.openclaw_send --channel whatsapp --target "+9199..." \
        --category hyd_fd_grit --km 42.5 --speed 32.8 --format chat
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

DEFAULT_API_BASE = os.getenv("AERO_API_BASE", "http://127.0.0.1:8000")
REQUEST_TIMEOUT_S = 20

CATEGORIES = [
    "bandok_classic",
    "hyd_fd_grit",
    "basso_aero",
    "pain_cave",
    "witty_sarcasm",
    "zen_filosofia",
    "chai_recovery",
]

# CLI name -> QuoteItem field holding the ready-to-send text.
FORMATS = {
    "title": "strava_title",
    "full": "strava_description",
    "status": "whatsapp_status",
    "chat": "whatsapp_chat",
}

CYAN, GREEN, YELLOW, RED, BOLD, RESET = (
    "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[1m", "\033[0m",
)


def fetch_quote(api_base: str, payload: dict) -> dict:
    """POST /api/generate and return the primary quote."""
    url = f"{api_base.rstrip('/')}/api/generate"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_S) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:400]
        raise SystemExit(f"{RED}✖ API {exc.code} from {url}: {detail}{RESET}")
    except urllib.error.URLError as exc:
        raise SystemExit(
            f"{RED}✖ Cannot reach {url} ({exc.reason}).{RESET}\n"
            f"  Start the app locally, or point --api-base at your deployed URL."
        )
    return body["primary"]


def send_via_openclaw(
    text: str, channel: str, target: str, dry_run: bool, media: list[str] | None
) -> None:
    """Hand the caption to `openclaw message send`."""
    binary = shutil.which("openclaw")
    if not binary:
        raise SystemExit(
            f"{RED}✖ `openclaw` not on PATH.{RESET}\n"
            f"  Install it with: npm install -g openclaw"
        )

    command = [binary, "message", "send", "--channel", channel, "--target", target,
               "--message", text]
    for item in media or []:
        command += ["--media", item]
    if dry_run:
        command.append("--dry-run")

    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        raise SystemExit(
            f"{RED}✖ openclaw exited {result.returncode}{RESET}\n"
            f"{result.stderr.strip() or '(no stderr)'}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send an AERO·HUD caption to a chat app via OpenClaw."
    )
    parser.add_argument("--api-base", default=DEFAULT_API_BASE,
                        help=f"AERO·HUD base URL (default: {DEFAULT_API_BASE})")
    parser.add_argument("--channel", default=os.getenv("OPENCLAW_CHANNEL"),
                        help="OpenClaw channel, e.g. whatsapp or telegram")
    parser.add_argument("-t", "--target", default=os.getenv("OPENCLAW_TARGET"),
                        help="Recipient: E.164 for WhatsApp/Signal, chat id for Telegram")
    parser.add_argument("-c", "--category", choices=CATEGORIES, default=None,
                        help="Vibe category")
    parser.add_argument("--format", choices=list(FORMATS), default="chat",
                        help="Which prepared caption to send (default: chat)")
    parser.add_argument("--km", type=float, default=None, help="Distance in km")
    parser.add_argument("--speed", type=float, default=None, help="Avg speed in km/h")
    parser.add_argument("--elev", type=int, default=None, help="Elevation in meters")
    parser.add_argument("--loc", type=str, default=None, help="Route/Location")
    parser.add_argument("--bike", type=str, default=None, help="Bicycle model")
    parser.add_argument("--media", action="append", default=None,
                        help="Attach a local path or URL; repeat for multiple")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the caption and payload without delivering")
    parser.add_argument("--quiet", action="store_true", help="Suppress the preview")

    args = parser.parse_args()

    if not args.channel or not args.target:
        parser.error(
            "--channel and --target are required "
            "(or set OPENCLAW_CHANNEL / OPENCLAW_TARGET)"
        )

    telemetry = {
        "distance_km": args.km,
        "avg_speed_kph": args.speed,
        "elevation_m": args.elev,
    }
    if args.loc:
        telemetry["location"] = args.loc
    if args.bike:
        telemetry["bike"] = args.bike

    quote = fetch_quote(args.api_base, {
        "category": args.category,
        "telemetry": telemetry,
        "count": 1,
    })
    text = quote[FORMATS[args.format]]

    if not args.quiet:
        print(f"\n{BOLD}{CYAN}⚡ AERO·HUD → OPENCLAW{RESET}")
        print(f"{YELLOW}Vibe:{RESET}    {quote['source_vibe']}")
        print(f"{YELLOW}Route:{RESET}   {args.channel} → {args.target}")
        print(f"{YELLOW}Format:{RESET}  {args.format} ({len(text)} chars)")
        print("─" * 50)
        print(text)
        print("─" * 50)

    send_via_openclaw(text, args.channel, args.target, args.dry_run, args.media)

    verb = "Previewed (dry run)" if args.dry_run else "Delivered"
    print(f"{BOLD}{GREEN}✔ {verb} via OpenClaw → {args.channel}{RESET}\n")


if __name__ == "__main__":
    main()
