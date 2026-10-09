"""Unit tests for TelemetryFormatter."""
from app.services.telemetry import TelemetryFormatter
from app.models.quote import RideTelemetry


def test_format_strava_title_length():
    short_title = "Never half-ass two things."
    assert TelemetryFormatter.format_strava_title(short_title) == "Never half-ass two things"

    long_title = "This is an extremely long and verbose cycling quote designed to test truncation boundary limits for Strava activity titles"
    formatted = TelemetryFormatter.format_strava_title(long_title, max_chars=50)
    assert len(formatted) <= 50
    assert formatted.endswith("...")


def test_format_strava_description_with_telemetry():
    telemetry = RideTelemetry(
        distance_km=40.0,
        avg_speed_kph=31.5,
        elevation_m=200,
        location="Financial District Loop",
        bike="Basso Venta R",
    )
    desc = TelemetryFormatter.format_strava_description(
        headline="Whole damn planet wanted a piece of me",
        subtext="Headwinds at 5:30 AM",
        telemetry=telemetry,
        source_vibe="Bandók Vault",
    )
    assert "Distance: 40.0 km" in desc
    assert "Avg Speed: 31.5 km/h" in desc
    assert "#BassoVentaR" in desc
    assert "#FinancialDistrict" in desc


def test_format_whatsapp_status():
    status = TelemetryFormatter.format_whatsapp_status("Aero is everything")
    assert "🚴‍♂️" in status
    assert "#BassoVentaR" in status
    assert len(status) <= 139


def test_build_card_metadata():
    telemetry = RideTelemetry(
        distance_km=45.0,
        avg_speed_kph=33.0,
        location="Knowledge City",
        bike="Basso Venta R",
    )
    meta = TelemetryFormatter.build_card_metadata(
        headline="Speed is a habit",
        subtext="Knowledge City sprint",
        telemetry=telemetry,
        category="basso_aero",
        vibe="Aero Division",
    )
    assert meta["distance"] == "45.0 KM"
    assert meta["speed"] == "33.0 KM/H"
    assert meta["bike"] == "Basso Venta R"
    assert "timestamp" in meta
