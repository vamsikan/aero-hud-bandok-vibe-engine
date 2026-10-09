"""Dynamic quote generator templates.
Allows blending live ride telemetry (km, speed, elevation, location, bike)
with Bandók's sharp wit and Hyderabad cycling flair.
"""
from typing import List, Dict, Any
from app.models.quote import QuoteCategory

DYNAMIC_TEMPLATES: List[Dict[str, Any]] = [
    {
        "id_prefix": "dyn-spd",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Aero Telemetry // Speed Pulse",
        "headline_template": "{speed} km/h on the {bike}: Defying physics, dodging potholes in {location}.",
        "subtext_template": "Pushed {distance} km with {elevation}m elevation. Italian carbon asked for more; legs declined.",
        "tags": ["telemetry", "speed", "basso", "aero"],
    },
    {
        "id_prefix": "dyn-hyd",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad Telemetry // FD Circuit",
        "headline_template": "{distance} km clocked around {location} before the city logged into Slack.",
        "subtext_template": "Suffering score: {suffer}/10. Average speed: {speed} km/h. Post-ride chai status: Essential.",
        "tags": ["hyderabad", "telemetry", "morning-hustle"],
    },
    {
        "id_prefix": "dyn-bdk",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Telemetry // Sarcastic Metrics",
        "headline_template": "They said 'easy ride.' {distance} km and {elevation}m of vertical deception later.",
        "subtext_template": "The Garmin doesn't lie, but my ride buddy certainly did.",
        "tags": ["bandok", "elevation", "deception", "garmin"],
    },
    {
        "id_prefix": "dyn-pn",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Threshold Telemetry",
        "headline_template": "{distance} km of pure zone 4 compliance across {location}.",
        "subtext_template": "Pushed {speed} km/h average. Lactate was high, morals were low, kudos are requested.",
        "tags": ["threshold", "zone4", "kudos", "cadence"],
    },
    {
        "id_prefix": "dyn-chi",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Chai Telemetry // Caloric Refuel",
        "headline_template": "{distance} km on the {bike} directly to {chai_count} cups of Irani chai.",
        "subtext_template": "Sustained {speed} km/h through {location} because hot chai waits for no cyclist.",
        "tags": ["chai", "refuel", "recovery", "hyderabad"],
    },
    {
        "id_prefix": "dyn-zen",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Telemetry // Morning Solitude",
        "headline_template": "{distance} km of quiet asphalt and early morning clarity in {location}.",
        "subtext_template": "{bike} rolling true. No traffic, no chaos, just sunrise and steady watts.",
        "tags": ["zen", "clarity", "morning", "watts"],
    },
]
