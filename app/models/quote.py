"""Domain models for quotes, telemetry, and generation payloads."""
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class QuoteCategory(str, Enum):
    """Categorization of cycling quotes inspired by Bandók and personal ride style."""
    BANDOK_CLASSIC = "bandok_classic"       # Cinematic, movie lines, witty banter
    HYD_FD_GRIT = "hyd_fd_grit"             # Financial District, Kokapet, Waverock, Cable Bridge, IT life
    BASSO_AERO = "basso_aero"               # Basso Venta R, Italian carbon, aero geometry, speed
    PAIN_CAVE = "pain_cave"                 # Lactate threshold, suffering, VO2 max, early mornings
    WITTY_SARCASM = "witty_sarcasm"         # Self-deprecating cyclist humor, Strava kudos chasing
    ZEN_FILOSOFIA = "zen_filosofia"         # The road, the machine, mental flow, morning stillness
    CHAI_RECOVERY = "chai_recovery"         # Post-ride Irani chai, Osmania biscuit, breakfast spins


class PlatformFormat(str, Enum):
    """Target output format."""
    STRAVA_TITLE = "strava_title"           # Short, witty title (<60 chars)
    STRAVA_FULL = "strava_full"             # Title + formatted telemetry + hashtags
    WHATSAPP_STATUS = "whatsapp_status"     # Short, punchy status with emojis (<130 chars)
    WHATSAPP_CHAT = "whatsapp_chat"         # Group broadcast with formatted telemetry


class RideTelemetry(BaseModel):
    """Optional telemetry from the ride to inject dynamic context."""
    distance_km: Optional[float] = Field(default=None, ge=0, le=500, description="Ride distance in kilometers")
    avg_speed_kph: Optional[float] = Field(default=None, ge=0, le=100, description="Average speed in km/h")
    elevation_m: Optional[int] = Field(default=None, ge=0, le=10000, description="Total elevation gain in meters")
    location: Optional[str] = Field(default="Financial District, Hyderabad", description="Route / Landmark")
    bike: Optional[str] = Field(default="Basso Venta R", description="Bicycle model")
    suffer_score: Optional[int] = Field(default=8, ge=1, le=10, description="Suffering rating from 1 to 10")
    chai_consumed: Optional[int] = Field(default=1, ge=0, le=10, description="Cups of Irani chai post-ride")


class QuoteItem(BaseModel):
    """Represents a generated or curated cycling quote."""
    id: str
    headline: str
    subtext: Optional[str] = None
    category: QuoteCategory
    source_vibe: str
    tags: List[str] = Field(default_factory=list)
    
    # Pre-formatted variants ready for 1-click clipboard
    strava_title: str
    strava_description: str
    whatsapp_status: str
    whatsapp_chat: str
    
    # HUD / Telemetry card data for rendering
    card_metadata: Dict[str, Any] = Field(default_factory=dict)


class GenerationRequest(BaseModel):
    """Payload to request quote generation."""
    category: Optional[QuoteCategory] = None
    telemetry: Optional[RideTelemetry] = None
    search_keyword: Optional[str] = None
    count: int = Field(default=1, ge=1, le=10)


class GenerationResponse(BaseModel):
    """Response payload containing primary quote and quick alternatives."""
    primary: QuoteItem
    alternatives: List[QuoteItem] = Field(default_factory=list)
    total_in_pool: int
    active_filters: Dict[str, Any] = Field(default_factory=dict)
