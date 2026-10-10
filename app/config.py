"""Application configuration and constants."""
import os
from typing import List
from pydantic import BaseModel


class Settings(BaseModel):
    """Core settings for AeroQuote / Bandók Engine."""
    APP_NAME: str = "AERO·HUD // Bandók Vibe Engine"
    VERSION: str = "2.0.4-aero"
    # Hosting platforms (Replit, Render, Fly, Heroku) inject these at runtime.
    DEBUG: bool = os.getenv("DEBUG", "").lower() in {"1", "true", "yes"}
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Default rider profile
    DEFAULT_BIKE: str = "Basso Venta R"
    DEFAULT_LOCATION: str = "Hyderabad - Financial District"
    DEFAULT_FREQUENCY: str = "4x / week"
    
    # Hyderabad FD landmarks
    HYD_LOCATIONS: List[str] = [
        "Kokapet Solar Roof Cycling Track",
        "Waverock Rolling Gradients",
        "Durgam Cheruvu Cable Bridge Sunrise",
        "Knowledge City Aero Strip",
        "Financial District - Gachibowli Loop",
        "Khajaguda Rock Climbs",
        "Nanakramguda Tech Corridor",
        "Bio-Diversity Flyover Sprint",
        "Niloufer Post-Ride Irani Chai Pitstop",
        "ORR Outer Ring Service Road TT",
    ]


settings = Settings()
