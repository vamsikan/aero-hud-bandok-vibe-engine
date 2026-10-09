"""Quote Generation and Personalization Engine."""
import random
import uuid
from typing import List, Optional, Dict, Any

from app.models.quote import (
    QuoteCategory,
    RideTelemetry,
    QuoteItem,
    GenerationRequest,
    GenerationResponse,
)
from app.data.quotes_db import RAW_QUOTES
from app.data.templates import DYNAMIC_TEMPLATES
from app.services.telemetry import TelemetryFormatter


class QuoteGeneratorService:
    """Core domain service for cycling quote generation and filtering."""

    def __init__(self):
        # In-memory working pool (can be dynamically extended)
        self._curated_quotes: List[Dict[str, Any]] = list(RAW_QUOTES)
        self._templates: List[Dict[str, Any]] = list(DYNAMIC_TEMPLATES)

    @property
    def total_quotes_count(self) -> int:
        return len(self._curated_quotes)

    def add_custom_quote(
        self,
        headline: str,
        subtext: Optional[str] = None,
        category: QuoteCategory = QuoteCategory.HYD_FD_GRIT,
        source_vibe: str = "Custom Rider Feed",
        tags: Optional[List[str]] = None,
    ) -> QuoteItem:
        """Add a custom quote into the active session pool."""
        new_entry = {
            "id": f"usr-{uuid.uuid4().hex[:6]}",
            "headline": headline,
            "subtext": subtext or "Locally curated rider wisdom.",
            "category": category,
            "source_vibe": source_vibe,
            "tags": tags or ["custom", "peloton"],
        }
        self._curated_quotes.insert(0, new_entry)
        return self._build_quote_item(new_entry, telemetry=None)

    def generate(self, request: Optional[GenerationRequest] = None) -> GenerationResponse:
        """Generate a primary quote and alternatives based on request filters."""
        req = request or GenerationRequest()
        telemetry = req.telemetry or RideTelemetry()

        # Step 1: Filter or search
        pool = self._filter_pool(
            category=req.category,
            search_keyword=req.search_keyword
        )

        # Step 2: Decide whether to inject dynamic template (if telemetry has custom stats)
        use_dynamic = (
            telemetry.distance_km is not None or 
            telemetry.avg_speed_kph is not None or
            (req.category in [QuoteCategory.BASSO_AERO, QuoteCategory.HYD_FD_GRIT] and random.random() > 0.6)
        )

        dynamic_item: Optional[QuoteItem] = None
        if use_dynamic:
            dynamic_item = self._generate_from_template(telemetry, req.category)

        # Step 3: Select candidates
        shuffled = list(pool)
        random.shuffle(shuffled)

        candidates: List[QuoteItem] = []
        if dynamic_item:
            candidates.append(dynamic_item)

        for raw in shuffled:
            if len(candidates) >= 4:
                break
            candidates.append(self._build_quote_item(raw, telemetry))

        if not candidates:
            # Fallback if search was too restrictive
            fallback_raw = random.choice(self._curated_quotes)
            candidates.append(self._build_quote_item(fallback_raw, telemetry))

        primary = candidates[0]
        alternatives = candidates[1:]

        return GenerationResponse(
            primary=primary,
            alternatives=alternatives,
            total_in_pool=len(self._curated_quotes),
            active_filters={
                "category": req.category.value if req.category else "all",
                "search_keyword": req.search_keyword,
                "telemetry_injected": bool(telemetry.distance_km or telemetry.avg_speed_kph),
            }
        )

    def get_all_categories(self) -> List[Dict[str, str]]:
        """Return human-readable metadata for all available categories."""
        labels = {
            QuoteCategory.BANDOK_CLASSIC: "Bandók Classic (Cinematic & Dry Wit)",
            QuoteCategory.HYD_FD_GRIT: "Morning Discipline (Dawn Patrol & Grit)",
            QuoteCategory.BASSO_AERO: "Basso Venta R Aero (Italian Carbon & Speed)",
            QuoteCategory.PAIN_CAVE: "Pain Cave (Threshold Suffering & Discipline)",
            QuoteCategory.WITTY_SARCASM: "Witty Sarcasm (Strava & Cyclist Reality)",
            QuoteCategory.ZEN_FILOSOFIA: "Zen & Filosofia (Morning Flow & Solitude)",
            QuoteCategory.CHAI_RECOVERY: "Chai Recovery (Irani Chai & Osmania Biscuits)",
        }
        return [
            {"id": cat.value, "label": labels.get(cat, cat.value.replace("_", " ").title())}
            for cat in QuoteCategory
        ]

    def _filter_pool(
        self,
        category: Optional[QuoteCategory] = None,
        search_keyword: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        pool = self._curated_quotes

        if category:
            pool = [q for q in pool if q["category"] == category]

        if search_keyword:
            kw = search_keyword.lower().strip()
            pool = [
                q for q in pool
                if kw in q["headline"].lower()
                or (q.get("subtext") and kw in q["subtext"].lower())
                or any(kw in tag.lower() for tag in q.get("tags", []))
            ]

        return pool if pool else self._curated_quotes

    def _generate_from_template(
        self,
        telemetry: RideTelemetry,
        category: Optional[QuoteCategory]
    ) -> Optional[QuoteItem]:
        """Interpolate telemetry into a dynamic template."""
        matching_templates = self._templates
        if category:
            matched = [t for t in self._templates if t["category"] == category]
            if matched:
                matching_templates = matched

        tmpl = random.choice(matching_templates)

        headline = tmpl["headline_template"]
        subtext = tmpl.get("subtext_template", "")

        raw = {
            "id": f"{tmpl['id_prefix']}-{uuid.uuid4().hex[:4]}",
            "headline": headline,
            "subtext": subtext,
            "category": tmpl["category"],
            "source_vibe": tmpl["source_vibe"],
            "tags": tmpl["tags"] + ["dynamic-telemetry"],
        }
        return self._build_quote_item(raw, telemetry)

    def _build_quote_item(
        self,
        raw: Dict[str, Any],
        telemetry: Optional[RideTelemetry]
    ) -> QuoteItem:
        """Compose a full QuoteItem with platform-formatted strings."""
        headline = raw["headline"]
        subtext = raw.get("subtext")
        vibe = raw.get("source_vibe", "Bandók Engine")
        category = raw["category"]
        tags = raw.get("tags", [])

        strava_title = TelemetryFormatter.format_strava_title(headline)
        strava_desc = TelemetryFormatter.format_strava_description(
            headline=headline,
            subtext=subtext,
            telemetry=telemetry,
            source_vibe=vibe,
        )
        wa_status = TelemetryFormatter.format_whatsapp_status(headline, telemetry)
        wa_chat = TelemetryFormatter.format_whatsapp_chat(headline, subtext, telemetry)
        card_meta = TelemetryFormatter.build_card_metadata(
            headline=headline,
            subtext=subtext,
            telemetry=telemetry,
            category=category.value if isinstance(category, QuoteCategory) else str(category),
            vibe=vibe,
        )

        return QuoteItem(
            id=raw["id"],
            headline=headline,
            subtext=subtext,
            category=category,
            source_vibe=vibe,
            tags=tags,
            strava_title=strava_title,
            strava_description=strava_desc,
            whatsapp_status=wa_status,
            whatsapp_chat=wa_chat,
            card_metadata=card_meta,
        )


# Global singleton instance
quote_generator_service = QuoteGeneratorService()
