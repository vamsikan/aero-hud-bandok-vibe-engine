"""REST API router for quote generation and telemetry."""
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from app.models.quote import (
    QuoteCategory,
    RideTelemetry,
    GenerationRequest,
    GenerationResponse,
    QuoteItem,
)
from app.services.generator import quote_generator_service
from app.config import settings

router = APIRouter(prefix="/api", tags=["Aero Quotes"])


class CustomQuotePayload(BaseModel):
    headline: str
    subtext: Optional[str] = None
    category: QuoteCategory = QuoteCategory.HYD_FD_GRIT
    tags: Optional[List[str]] = None


@router.post("/generate", response_model=GenerationResponse)
async def generate_quote(request: GenerationRequest):
    """Generate primary quote and alternatives matching criteria."""
    try:
        return quote_generator_service.generate(request)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/random", response_model=QuoteItem)
async def get_random_quote(
    category: Optional[QuoteCategory] = Query(None, description="Optional category filter")
):
    """Fetch a single random quote quickly."""
    req = GenerationRequest(category=category)
    res = quote_generator_service.generate(req)
    return res.primary


@router.get("/categories")
async def list_categories():
    """List available categories and descriptive metadata."""
    return {
        "categories": quote_generator_service.get_all_categories()
    }


@router.get("/landmarks")
async def list_landmarks() -> List[str]:
    """List Hyderabad Financial District cycling landmarks."""
    return settings.HYD_LOCATIONS


@router.post("/quotes/custom", response_model=QuoteItem)
async def create_custom_quote(payload: CustomQuotePayload):
    """Add a rider's custom quote into the live engine."""
    if not payload.headline.strip():
        raise HTTPException(status_code=400, detail="Headline cannot be empty")
    
    return quote_generator_service.add_custom_quote(
        headline=payload.headline,
        subtext=payload.subtext,
        category=payload.category,
        tags=payload.tags,
    )


@router.get("/stats")
async def get_engine_stats():
    """System and repository telemetry stats."""
    return {
        "app_name": settings.APP_NAME,
        "version": settings.VERSION,
        "default_bike": settings.DEFAULT_BIKE,
        "location": settings.DEFAULT_LOCATION,
        "total_curated_quotes": quote_generator_service.total_quotes_count,
        "categories_count": len(QuoteCategory),
    }
