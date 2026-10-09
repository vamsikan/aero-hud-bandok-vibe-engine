"""Command Line Interface for AeroQuote // Bandók Engine.
Allows rapid terminal generation and direct copy to macOS clipboard.
"""
import argparse
import subprocess
import sys
from app.models.quote import QuoteCategory, RideTelemetry, GenerationRequest
from app.services.generator import quote_generator_service


def copy_to_macos_clipboard(text: str) -> bool:
    """Copy text to macOS clipboard using pbcopy if available."""
    try:
        process = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
        process.communicate(text.encode("utf-8"))
        return process.returncode == 0
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="AERO·HUD CLI - Instant Strava & WhatsApp cycling caption generator."
    )
    parser.add_argument(
        "-c", "--category",
        choices=[c.value for c in QuoteCategory],
        default=None,
        help="Vibe category"
    )
    parser.add_argument("--km", type=float, default=None, help="Distance in km")
    parser.add_argument("--speed", type=float, default=None, help="Avg speed in km/h")
    parser.add_argument("--elev", type=int, default=None, help="Elevation in meters")
    parser.add_argument("--loc", type=str, default="Financial District, Hyderabad", help="Route/Location")
    parser.add_argument("--bike", type=str, default="Basso Venta R", help="Bicycle model")
    parser.add_argument("--format", choices=["strava", "wa", "full"], default="strava", help="Output format")
    parser.add_argument("--copy", action="store_true", default=True, help="Auto-copy to clipboard")

    args = parser.parse_args()

    telemetry = RideTelemetry(
        distance_km=args.km,
        avg_speed_kph=args.speed,
        elevation_m=args.elev,
        location=args.loc,
        bike=args.bike,
    )

    req = GenerationRequest(
        category=QuoteCategory(args.category) if args.category else None,
        telemetry=telemetry
    )

    res = quote_generator_service.generate(req)
    quote = res.primary

    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    bold = "\033[1m"
    reset = "\033[0m"

    print(f"\n{bold}{cyan}⚡ AERO·HUD // BANDÓK VIBE ENGINE{reset}")
    print(f"{yellow}Vibe:{reset} {quote.source_vibe}")
    print(f"{bold}Headline:{reset} {quote.headline}")
    if quote.subtext:
        print(f"{bold}Subtext:{reset}  {quote.subtext}")
    print("─" * 50)

    if args.format == "strava":
        output = quote.strava_title
        print(f"{bold}{green}Strava Title:{reset}\n{output}")
    elif args.format == "wa":
        output = quote.whatsapp_status
        print(f"{bold}{green}WhatsApp Status:{reset}\n{output}")
    else:
        output = quote.strava_description
        print(f"{bold}{green}Strava Full Card:{reset}\n{output}")

    if args.copy and sys.platform == "darwin":
        if copy_to_macos_clipboard(output):
            print(f"\n{bold}{green}✔ Copied directly to macOS clipboard!{reset}\n")


if __name__ == "__main__":
    main()
