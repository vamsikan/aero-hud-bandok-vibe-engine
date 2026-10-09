"""Unit tests for QuoteGeneratorService."""
from app.services.generator import QuoteGeneratorService
from app.models.quote import QuoteCategory, GenerationRequest, RideTelemetry


def test_generator_service_initialization():
    service = QuoteGeneratorService()
    assert service.total_quotes_count > 0


def test_generator_filter_by_category():
    service = QuoteGeneratorService()
    req = GenerationRequest(category=QuoteCategory.BASSO_AERO)
    res = service.generate(req)
    
    assert res.primary.category == QuoteCategory.BASSO_AERO
    assert res.active_filters["category"] == "basso_aero"


def test_generator_keyword_search():
    service = QuoteGeneratorService()
    req = GenerationRequest(search_keyword="chai")
    res = service.generate(req)
    
    # Should find chai-related quote or fallback gracefully
    assert "chai" in res.primary.headline.lower() or "chai" in (res.primary.subtext or "").lower() or any("chai" in t for t in res.primary.tags)


def test_generator_dynamic_telemetry_interpolation():
    service = QuoteGeneratorService()
    telemetry = RideTelemetry(
        distance_km=55.0,
        avg_speed_kph=34.2,
        elevation_m=310,
        location="Kokapet Solar Roof",
        bike="Basso Venta R",
    )
    req = GenerationRequest(telemetry=telemetry, category=QuoteCategory.BASSO_AERO)
    res = service.generate(req)
    
    # Check that telemetry metadata was attached
    assert res.primary.card_metadata["distance"] == "55.0 KM"
    assert res.primary.card_metadata["speed"] == "34.2 KM/H"
    assert res.primary.card_metadata["bike"] == "Basso Venta R"


def test_add_custom_quote():
    service = QuoteGeneratorService()
    initial_count = service.total_quotes_count
    
    custom = service.add_custom_quote(
        headline="Kokapet sprint was legendary today.",
        subtext="Pushed 400 watts past the tech towers.",
        category=QuoteCategory.HYD_FD_GRIT,
    )
    
    assert service.total_quotes_count == initial_count + 1
    assert custom.headline == "Kokapet sprint was legendary today."
    assert custom.category == QuoteCategory.HYD_FD_GRIT
