"""Dynamic quote generator templates.
Pure thematic templates without location names or raw data metrics.
"""
from typing import List, Dict, Any
from app.models.quote import QuoteCategory

DYNAMIC_TEMPLATES: List[Dict[str, Any]] = [
    {
        "id_prefix": "dyn-spd",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Aero Telemetry // Speed Pulse",
        "headline_template": "Out of the saddle, into the drops, past all reasonable excuses.",
        "subtext_template": "Italian carbon demanded race pace; legs offered sheer stubborn compliance.",
        "tags": ["telemetry", "speed", "basso", "aero"],
    },
    {
        "id_prefix": "dyn-grt",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Dawn Pelotón // Morning Circuit",
        "headline_template": "The alarm was unreasonable, the wind was disrespectful, the ride was glorious.",
        "subtext_template": "Pedaled through the morning mist before the world even logged into Slack.",
        "tags": ["morning-hustle", "dawn", "grit"],
    },
    {
        "id_prefix": "dyn-bdk",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Telemetry // Sarcastic Flow",
        "headline_template": "They promised an easy recovery spin. That was a hilarious piece of fiction.",
        "subtext_template": "The GPS does not lie, but my riding buddy certainly did.",
        "tags": ["bandok", "fiction", "deception", "recovery"],
    },
    {
        "id_prefix": "dyn-pn",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Threshold Gospel",
        "headline_template": "Voluntary distress in the big ring. Kudos gratefully accepted.",
        "subtext_template": "Lactate was abundant, dignity was compromised, cadence remained defiant.",
        "tags": ["threshold", "zone4", "kudos", "cadence"],
    },
    {
        "id_prefix": "dyn-chi",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Chai Telemetry // Caloric Refuel",
        "headline_template": "Riding hard in the morning solely to justify double-patti chai and biscuits.",
        "subtext_template": "Caloric math is simple when the tea is hot and the pedals are resting.",
        "tags": ["chai", "refuel", "recovery"],
    },
    {
        "id_prefix": "dyn-zen",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Telemetry // Morning Solitude",
        "headline_template": "Empty asphalt, silent horizon, and the quiet truth of two spinning wheels.",
        "subtext_template": "No traffic, no chaos, just the morning sunrise and steady cadence.",
        "tags": ["zen", "clarity", "morning", "watts"],
    },
]
