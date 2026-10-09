"""Telemetry formatting utilities for Strava and WhatsApp."""
from typing import Dict, Any, Optional
from datetime import datetime
from app.models.quote import RideTelemetry


class TelemetryFormatter:
    """Formats quotes and ride metrics into platform-specific syntaxes."""

    @staticmethod
    def format_strava_title(headline: str, max_chars: int = 55) -> str:
        """Create a punchy, Bandók-style Strava activity title."""
        cleaned = headline.strip().rstrip(".")
        if len(cleaned) <= max_chars:
            return cleaned
        # Truncate at word boundary
        truncated = cleaned[:max_chars - 3].rsplit(" ", 1)[0] + "..."
        return truncated

    @staticmethod
    def format_strava_description(
        headline: str,
        subtext: Optional[str],
        telemetry: Optional[RideTelemetry] = None,
        source_vibe: str = "Bandók Engine"
    ) -> str:
        """Create a full Strava activity description with telemetry & tags."""
        lines = [headline]
        if subtext:
            lines.append(f"\n{subtext}")
            
        lines.append("\n━━━━━━━━━━━━━━━━━━━━")
        if telemetry:
            telemetry_entries = []
            if telemetry.distance_km is not None:
                telemetry_entries.append(f"📍 Distance: {telemetry.distance_km:.1f} km")
            if telemetry.avg_speed_kph is not None:
                telemetry_entries.append(f"⚡ Avg Speed: {telemetry.avg_speed_kph:.1f} km/h")
            if telemetry.elevation_m is not None:
                telemetry_entries.append(f"⛰️ Elevation: {telemetry.elevation_m} m")
            if telemetry.suffer_score is not None:
                telemetry_entries.append(f"🔥 Suffer Score: {telemetry.suffer_score}/10")
            if telemetry.location:
                telemetry_entries.append(f"🗺️ Route: {telemetry.location}")
            if telemetry.bike:
                telemetry_entries.append(f"🚲 Steed: {telemetry.bike}")
            if telemetry.chai_consumed:
                telemetry_entries.append(f"☕ Irani Chai: {telemetry.chai_consumed} cups")

            if telemetry_entries:
                lines.extend(telemetry_entries)
                lines.append("━━━━━━━━━━━━━━━━━━━━")

        lines.append(f"📡 Vibe: {source_vibe}")
        lines.append("#BassoVentaR #HydCycling #FinancialDistrict #Bandók #ItalianAero")
        return "\n".join(lines)

    @staticmethod
    def format_whatsapp_status(headline: str, telemetry: Optional[RideTelemetry] = None) -> str:
        """Create a concise, punchy WhatsApp Status with emojis."""
        metric_badge = ""
        if telemetry and telemetry.distance_km:
            metric_badge = f" [{telemetry.distance_km:.0f}km ⚡] "
        
        status = f"🚴‍♂️ {headline}{metric_badge}🇮🇹 #BassoVentaR"
        if len(status) > 135:
            status = f"🚴‍♂️ {headline[:100]}... ⚡"
        return status

    @staticmethod
    def format_whatsapp_chat(
        headline: str,
        subtext: Optional[str],
        telemetry: Optional[RideTelemetry] = None
    ) -> str:
        """Format an aesthetic WhatsApp group chat message."""
        lines = [
            f"🚴‍♂️ *RIDE FINISHED // HYD FD CIRCUIT*",
            f"❝ *{headline}* ❞",
        ]
        if subtext:
            lines.append(f"_{subtext}_")
            
        if telemetry:
            stats = []
            if telemetry.distance_km:
                stats.append(f"• *Distance:* {telemetry.distance_km:.1f} km")
            if telemetry.avg_speed_kph:
                stats.append(f"• *Pace:* {telemetry.avg_speed_kph:.1f} km/h")
            if telemetry.elevation_m:
                stats.append(f"• *Climb:* {telemetry.elevation_m} m")
            if telemetry.location:
                stats.append(f"• *Loop:* {telemetry.location}")
            if telemetry.chai_consumed:
                stats.append(f"• *Irani Chai:* {telemetry.chai_consumed} ☕")
            if stats:
                lines.append("\n*Telemetry:*")
                lines.extend(stats)
                
        lines.append("\n🚲 _Basso Venta R | Hyderabad Pelotón_")
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
            "location": telemetry.location if telemetry and telemetry.location else "Financial District, Hyderabad",
            "bike": telemetry.bike if telemetry and telemetry.bike else "Basso Venta R",
            "category": category,
            "vibe": vibe,
            "timestamp": now_str,
        }
