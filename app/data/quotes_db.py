"""Curated repository of cycling quotes.
Inspired by Bandók (bandok.com) styling: movie quotes, dry wit, cycling suffering,
blended with Italian aero passion (Basso Venta R) and Hyderabad Financial District grit.
"""
from typing import List, Dict, Any
from app.models.quote import QuoteCategory

RAW_QUOTES: List[Dict[str, Any]] = [
    # =========================================================================
    # 1. BANDÓK CLASSIC (Movie lines, Pop culture, Dry wit, Iconic banter)
    # =========================================================================
    {
        "id": "bdk-001",
        "headline": "Whole damn planet wanted a piece of me.",
        "subtext": "Took every headwind personally today.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Cinematic Sarcasm",
        "tags": ["bandok", "grit", "cinematic", "headwind"],
    },
    {
        "id": "bdk-002",
        "headline": "Never half-ass two things. Whole-ass one bike ride.",
        "subtext": "Ron Swanson would approve of this cadence.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Parks & Rec Logic",
        "tags": ["bandok", "humor", "discipline", "effort"],
    },
    {
        "id": "bdk-003",
        "headline": "Destiny is the one doing the folding; we’re just the origami swans.",
        "subtext": "Folded neatly into the aero drops for 40 kilometers.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Existential Aero",
        "tags": ["bandok", "philosophical", "aero", "destiny"],
    },
    {
        "id": "bdk-004",
        "headline": "I paid for the whole speedometer, I’m using the whole speedometer.",
        "subtext": "Gravity was my chief sponsor on the descent.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Speed Chaser",
        "tags": ["bandok", "speed", "descent", "witty"],
    },
    {
        "id": "bdk-005",
        "headline": "If everything you try works, you’re not shifting into the big ring.",
        "subtext": "Cross-chaining my way through existential dread.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Big Ring Mentality",
        "tags": ["bandok", "gears", "effort", "grind"],
    },
    {
        "id": "bdk-006",
        "headline": "We’re the only species on Earth that observes lactate threshold.",
        "subtext": "Evolution didn't prepare my quads for this cadence.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Biology vs Bicycle",
        "tags": ["bandok", "biology", "legs", "lactate"],
    },
    {
        "id": "bdk-007",
        "headline": "Who turns down clean asphalt and questionable pacing?",
        "subtext": "Certainly not someone who woke up before sunrise.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Dawn Patrol",
        "tags": ["bandok", "sunrise", "pacing", "asphalt"],
    },
    {
        "id": "bdk-008",
        "headline": "My legs wrote a check that my heart rate couldn't cash.",
        "subtext": "Overdrafted in zone 5. Penalty fees paid in sweat.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Financial Ruin",
        "tags": ["bandok", "heart-rate", "zone5", "exhaustion"],
    },
    {
        "id": "bdk-009",
        "headline": "Tell the gradient I wasn't listening.",
        "subtext": "Out of the saddle. Defiant to the finish line.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Climb Defiance",
        "tags": ["bandok", "climbing", "attitude", "hills"],
    },
    {
        "id": "bdk-010",
        "headline": "Aerodynamics is a polite agreement between drag and stubbornness.",
        "subtext": "Today, stubbornness won by 2.4 seconds.",
        "category": QuoteCategory.BANDOK_CLASSIC,
        "source_vibe": "Bandók Vault // Wind Tunnel Logic",
        "tags": ["bandok", "aero", "physics", "stubborn"],
    },

    # =========================================================================
    # 2. HYDERABAD FINANCIAL DISTRICT GRIT (Local culture, FD, Kokapet, Cable Bridge)
    # =========================================================================
    {
        "id": "hyd-101",
        "headline": "Dodging corporate burnout and Kokapet dumpers simultaneously.",
        "subtext": "Financial District morning circuit: The true endurance test.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Morning Survival",
        "tags": ["hyderabad", "financial-district", "kokapet", "morning-ride"],
    },
    {
        "id": "hyd-102",
        "headline": "4 days a week on ORR service roads: Cheaper than therapy, faster than tech syncs.",
        "subtext": "Cleared my sprint backlog before the 9:30 AM standup.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Tech Corridor",
        "tags": ["hyderabad", "orr", "routine", "tech-life"],
    },
    {
        "id": "hyd-103",
        "headline": "Waverock gradient: Where IT architects learn what true structural stress means.",
        "subtext": "Heart rate higher than cloud hosting bills.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Waverock Climb",
        "tags": ["hyderabad", "waverock", "climb", "gradients"],
    },
    {
        "id": "hyd-104",
        "headline": "Cable Bridge at 5:45 AM hits different when your Garmin beeps 178 bpm.",
        "subtext": "Durgam Cheruvu glow fading as the big ring drops.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Cable Bridge Aero",
        "tags": ["hyderabad", "cable-bridge", "durgam-cheruvu", "garmin"],
    },
    {
        "id": "hyd-105",
        "headline": "The Kokapet Solar Cycling Track is green energy; my calves are pure nuclear fission.",
        "subtext": "Smooth tarmac beneath the panels, pure wattage above.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Solar Roof Track",
        "tags": ["hyderabad", "solar-track", "kokapet", "wattage"],
    },
    {
        "id": "hyd-106",
        "headline": "Knowledge City sprint: 0 knowledge gained, 100% lactic acid harvested.",
        "subtext": "Racing the IT shuttle buses and taking podium positions.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Knowledge City",
        "tags": ["hyderabad", "knowledge-city", "sprint", "speed"],
    },
    {
        "id": "hyd-107",
        "headline": "Beat the 8 AM Gachibowli gridlock by already being exhausted at 7 AM.",
        "subtext": "They're honking in traffic; I'm sipping hot Irani chai.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Gachibowli Flow",
        "tags": ["hyderabad", "gachibowli", "traffic", "early-bird"],
    },
    {
        "id": "hyd-108",
        "headline": "Khajaguda hills don't negotiate with your sprint cadence.",
        "subtext": "Standing on the pedals, chasing the sunrise over the IT towers.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Khajaguda Hills",
        "tags": ["hyderabad", "khajaguda", "hills", "sunrise"],
    },
    {
        "id": "hyd-109",
        "headline": "Nanakramguda roundabout is my velodrome, the morning fog is my spectator.",
        "subtext": "Turning FD asphalt into personal time-trial territory.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Nanakramguda TT",
        "tags": ["hyderabad", "nanakramguda", "fog", "crit"],
    },
    {
        "id": "hyd-110",
        "headline": "Bio-Diversity flyover descent: Reaching orbital velocity before Hyderabad wakes up.",
        "subtext": "Aero tucked past the sleeping glass-facade towers.",
        "category": QuoteCategory.HYD_FD_GRIT,
        "source_vibe": "Hyderabad FD Pelotón // Flyover Aero",
        "tags": ["hyderabad", "biodiversity", "descent", "speed"],
    },

    # =========================================================================
    # 3. BASSO VENTA R AERO (Italian racing heritage, geometry, carbon stiffness)
    # =========================================================================
    {
        "id": "bso-201",
        "headline": "Italian carbon doesn't know what a casual recovery pace means.",
        "subtext": "Basso Venta R demanded race pace; my lungs offered compliance.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Italian Racing Soul",
        "tags": ["basso", "venta-r", "italian", "carbon", "aero"],
    },
    {
        "id": "bso-202",
        "headline": "Basso Venta R: 8.5 kg of Italian precision, 75 kg of questionable decisions.",
        "subtext": "Designed in Bassano del Grappa, unleashed on Financial District tarmac.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Race Precision",
        "tags": ["basso", "venta-r", "weight", "engineering"],
    },
    {
        "id": "bso-203",
        "headline": "Aggressive geometry because my spine was getting far too comfortable with desk work.",
        "subtext": "Slammed the stem. Aero gains over lumbar sympathy.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Cockpit Aggression",
        "tags": ["basso", "geometry", "drops", "slammed-stem"],
    },
    {
        "id": "bso-204",
        "headline": "Microtech wheels humming at 36 km/h. Pure Italian mechanical orchestra.",
        "subtext": "No playlist required when the hub engagement sounds like a swarm of wasps.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Hub Acoustics",
        "tags": ["basso", "microtech", "wheels", "sound"],
    },
    {
        "id": "bso-205",
        "headline": "The Venta R slices the wind; I just hold on and try not to embarrass the badge.",
        "subtext": "Handcrafted pedigree meets amateur morning enthusiasm.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Aero Aerodynamics",
        "tags": ["basso", "venta-r", "pedigree", "wind"],
    },
    {
        "id": "bso-206",
        "headline": "Toray carbon stiffness: Every watt delivered directly to the asphalt, no refund asked.",
        "subtext": "Power transfer so direct my quads filed a complaint.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Bottom Bracket Power",
        "tags": ["basso", "carbon", "wattage", "stiffness"],
    },
    {
        "id": "bso-207",
        "headline": "Look fast, suffer faster. The Italian racing doctrine.",
        "subtext": "If the bike looks like a missile, you can't ride it like a commuter.",
        "category": QuoteCategory.BASSO_AERO,
        "source_vibe": "Bassano del Grappa // Pure Aesthetics",
        "tags": ["basso", "speed", "style", "italian-style"],
    },

    # =========================================================================
    # 4. PAIN CAVE & SUFFERING (Lactate threshold, VO2 Max, 4-days discipline)
    # =========================================================================
    {
        "id": "pn-301",
        "headline": "Suffering is temporary, Strava kudos are semi-permanent.",
        "subtext": "Heart rate redlined, dignity compromised, segment matched.",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Threshold Gospel",
        "tags": ["suffering", "strava", "kudos", "threshold"],
    },
    {
        "id": "pn-302",
        "headline": "Entered the pain cave at 5:30 AM. Renovated it, put up curtains, stayed for sprints.",
        "subtext": "Zone 4 is my permanent residential address.",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Zone 4 Leaseholder",
        "tags": ["pain-cave", "sprints", "zone4", "morning"],
    },
    {
        "id": "pn-303",
        "headline": "Breathing through my ears and pedaling with pure remorse.",
        "subtext": "Why do we pay good money to voluntarily torture ourselves before dawn?",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Existential Suffer",
        "tags": ["suffering", "lungs", "dawn", "cycling-life"],
    },
    {
        "id": "pn-304",
        "headline": "My Garmin asked if I wanted to record an emergency event; I said no, it’s just a 3% incline.",
        "subtext": "Cadence dropped, ego followed closely behind.",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Incline Reality",
        "tags": ["garmin", "incline", "heart-rate", "humor"],
    },
    {
        "id": "pn-305",
        "headline": "4 days a week of voluntary cardiovascular bankruptcy.",
        "subtext": "My alarm clock is my biggest rival, and the pedals are my court of appeals.",
        "category": QuoteCategory.PAIN_CAVE,
        "source_vibe": "Pain Cave // Consistency Irony",
        "tags": ["discipline", "consistency", "alarm", "quitting-not-an-option"],
    },

    # =========================================================================
    # 5. WITTY SARCASM & CYCLIST REALITY
    # =========================================================================
    {
        "id": "wit-401",
        "headline": "It's not a mid-life crisis if it has disc brakes and an integrated cockpit.",
        "subtext": "It’s a high-performance mental health investment.",
        "category": QuoteCategory.WITTY_SARCASM,
        "source_vibe": "Bike Geek // Justification Protocol",
        "tags": ["sarcasm", "n+1", "cockpit", "investment"],
    },
    {
        "id": "wit-402",
        "headline": "If it’s not on Strava, did the lactic acid even happen?",
        "subtext": "Phone battery survived, Garmin synced, existence validated.",
        "category": QuoteCategory.WITTY_SARCASM,
        "source_vibe": "Bike Geek // Strava Ontology",
        "tags": ["strava", "sync", "validation", "gps"],
    },
    {
        "id": "wit-403",
        "headline": "My diet is 70% aero denial and 30% electrolyte delusion.",
        "subtext": "Spent 20 minutes saving 4 watts in clothing, ate two samosas later.",
        "category": QuoteCategory.WITTY_SARCASM,
        "source_vibe": "Bike Geek // Aero Delusion",
        "tags": ["sarcasm", "nutrition", "aero-watts", "food"],
    },
    {
        "id": "wit-404",
        "headline": "I told myself I’d do a gentle recovery spin. That was a hilarious lie.",
        "subtext": "Spotted another cyclist 200m ahead. The race was declared.",
        "category": QuoteCategory.WITTY_SARCASM,
        "source_vibe": "Bike Geek // The Unspoken Race",
        "tags": ["recovery-spin", "lie", "chase", "peloton"],
    },
    {
        "id": "wit-405",
        "headline": "Chain lube, chamois cream, and reckless optimism.",
        "subtext": "The Holy Trinity of amateur road cycling.",
        "category": QuoteCategory.WITTY_SARCASM,
        "source_vibe": "Bike Geek // Essentials",
        "tags": ["gear", "optimism", "roadie", "humor"],
    },

    # =========================================================================
    # 6. ZEN & FILOSOFIA (Mental flow, The road, Quiet mornings)
    # =========================================================================
    {
        "id": "zen-501",
        "headline": "The rhythm of two wheels silences the noise of ten thousand thoughts.",
        "subtext": "Sunrise over Hyderabad's skyline. Just tire hum and breath.",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Road // Mindflow",
        "tags": ["zen", "mindfulness", "sunrise", "clarity"],
    },
    {
        "id": "zen-502",
        "headline": "You don't ride to escape life; you ride so life doesn't escape you.",
        "subtext": "Early morning pedal strokes reclaiming the hours before the screen takes over.",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Road // Existential Pace",
        "tags": ["zen", "presence", "life", "freedom"],
    },
    {
        "id": "zen-503",
        "headline": "Every pedal stroke is a quiet negotiation with gravity and yourself.",
        "subtext": "Nothing forced. Just steady cadence on smooth Italian carbon.",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Road // Flow State",
        "tags": ["zen", "cadence", "harmony", "meditation"],
    },
    {
        "id": "zen-504",
        "headline": "The road never lies. It returns exactly what you put into the pedals.",
        "subtext": "Empty tarmac at dawn is the cleanest mirror in the world.",
        "category": QuoteCategory.ZEN_FILOSOFIA,
        "source_vibe": "Zen Road // Pure Honesty",
        "tags": ["zen", "truth", "road", "dawn"],
    },

    # =========================================================================
    # 7. CHAI RECOVERY & HYDERABAD POST-RIDE RITUAL
    # =========================================================================
    {
        "id": "chi-601",
        "headline": "Powered by Italian engineering, refueled by boiling Irani Chai & Osmania biscuits.",
        "subtext": "The only true metric that matters: Wattage-to-Chai ratio.",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Deccan Pelotón // Chai Pitstop",
        "tags": ["chai", "irani-chai", "osmania", "hyderabad", "recovery"],
    },
    {
        "id": "chi-602",
        "headline": "Did 45 km just to justify dipping three Osmania biscuits in double-patti chai.",
        "subtext": "Caloric math: 1000 burned, 1200 reclaimed with zero regrets.",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Deccan Pelotón // Caloric Balance",
        "tags": ["chai", "osmania-biscuit", "calories", "guilt-free"],
    },
    {
        "id": "chi-603",
        "headline": "Niloufer pitstop: Where the Basso leans against the wall and the legs finally stop shaking.",
        "subtext": "Steam rising from the cup, sweat drying on the jersey.",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Deccan Pelotón // Niloufer Sanctuary",
        "tags": ["niloufer", "chai", "recovery", "basso", "community"],
    },
    {
        "id": "chi-604",
        "headline": "Strava pause button activated solely for cutting chai protocol.",
        "subtext": "Garmin auto-pause respects the culture.",
        "category": QuoteCategory.CHAI_RECOVERY,
        "source_vibe": "Deccan Pelotón // Auto-Pause Culture",
        "tags": ["auto-pause", "chai", "culture", "garmin"],
    },
]
