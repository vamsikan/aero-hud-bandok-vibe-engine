"""Unit tests for domain models."""
import pytest
from pydantic import ValidationError

from app.models.quote import (
    QuoteCategory,
    PlatformFormat,
    RideTelemetry,
    QuoteItem,
    GenerationRequest,
    GenerationResponse,
)


def test_ride_telemetry_valid():
    """Verify valid telemetry instantiation and defaults."""
    telemetry = RideTelemetry(
        distance_km=42.5,
        avg_speed_kph=32.1,
        elevation_m=280,
        location="Waverock Climbs",
        bike="Basso Venta R",
        suffer_score=9,
        chai_consumed=2,
    )
    assert telemetry.distance_km == 42.5
    assert telemetry.bike == "Basso Venta R"
    assert telemetry.suffer_score == 9


def test_ride_telemetry_validation_bounds():
    """Verify validation boundaries on distance and suffer score."""
    with pytest.raises(ValidationError):
        RideTelemetry(distance_km=-10)

    with pytest.raises(ValidationError):
        RideTelemetry(suffer_score=15)  # Max is 10


def test_quote_item_structure():
    """Verify QuoteItem schema serialization."""
    item = QuoteItem(
        id="test-123",
        headline="Whole damn planet wanted a piece of me.",
        subtext="Headwinds at 5:30 AM.",
        category=QuoteCategory.BANDOK_CLASSIC,
        source_vibe="Bandók Vault",
        tags=["bandok", "grit"],
        strava_title="Whole damn planet wanted a piece of me",
        strava_description="Full activity block",
        whatsapp_status="🚴‍♂️ Status",
        whatsapp_chat="Broadcast block",
        card_metadata={"distance": "42 KM"},
    )
    assert item.id == "test-123"
    assert item.category == QuoteCategory.BANDOK_CLASSIC
    assert "bandok" in item.tags
