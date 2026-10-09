"""Telemetry formatting utilities for Strava and WhatsApp.
Ensures quotes remain 100% pure without embedded locations or data metrics.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from app.models.quote import RideTelemetry


class TelemetryFormatter:
    """Formats quotes into platform-specific syntaxes without polluting the quote text."""

    @staticmethod
    def format_strava_title(headline: str, max_chars: int = 55) -> str:
        """Create a punchy, pure Bandók-style Strava activity title without numbers or locations."""
        cleaned = headline.strip().rstrip(".")
        if len(cleaned) <= max_chars:
            return cleaned
        # Truncate cleanly at word boundary
        truncated = cleaned[:max_chars - 3].rsplit(" ", 1)[0] + "..."
        return truncated

    @staticmethod
    def format_strava_description(
        headline: str,
        subtext: Optional[str],
        telemetry: Optional[RideTelemetry] = None,
        source_vibe: str = "Bandók Engine"
    ) -> str:
        """Create a full Strava description: Pure quote on top, optional gear/tags below."""
        lines = [headline]
        if subtext:
            lines.append(f"\n\"{subtext}\"")
            
        lines.append("\n━━━━━━━━━━━━━━━━━━━━")
        lines.append(f"📡 Vibe: {source_vibe}")
        lines.append("🚲 Steed: Basso Venta R 🇮🇹")
        lines.append("#BassoVentaR #Bandók #RoadCycling #Peloton #ItalianAero")
        return "\n".join(lines)

    @staticmethod
    def format_whatsapp_status(headline: str, telemetry: Optional[RideTelemetry] = None) -> str:
        """Create a pure, punchy WhatsApp Status with zero numbers or locations."""
        status = f"🚴‍♂️ {headline} 🇮🇹"
        if len(status) > 135:
            status = f"🚴‍♂️ {headline[:115]}... ⚡"
        return status

    @staticmethod
    def format_whatsapp_chat(
        headline: str,
        subtext: Optional[str],
        telemetry: Optional[RideTelemetry] = None
    ) -> str:
        """Format an aesthetic WhatsApp group chat message."""
        lines = [
            f"🚴‍♂️ *RIDE COMPLETE // MORNING PELOTÓN*",
            f"❝ *{headline}* ❞",
        ]
        if subtext:
            lines.append(f"_{subtext}_")
                
        lines.append("\n🚲 _Basso Venta R | Italian Aero_")
        return "\n".join(lines)

    @staticmethod
    def build_card_metadata(
        headline: str,
        subtext: Optional[str],
        telemetry: Optional[RideTelemetry],
        category: str,
        vibe: str
    ) -> Dict[str, Any]:
        """Telemetry metadata utilized by canvas card generator."""
        now_str = datetime.now().strftime("%Y-%m-%d // %H:%M")
        return {
            "headline": headline,
            "subtext": subtext or "",
            "distance": f"{telemetry.distance_km:.1f} KM" if telemetry and telemetry.distance_km else "42.0 KM",
            "speed": f"{telemetry.avg_speed_kph:.1f} KM/H" if telemetry and telemetry.avg_speed_kph else "31.4 KM/H",
            "elevation": f"{telemetry.elevation_m} M" if telemetry and telemetry.elevation_m else "240 M",
            "location": "Morning Pelotón",
            "bike": telemetry.bike if telemetry and telemetry.bike else "Basso Venta R",
            "category": category,
            "vibe": vibe,
            "timestamp": now_str,
        }
