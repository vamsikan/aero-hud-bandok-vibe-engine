# 🚴‍♂️ AERO·HUD // Bandók Vibe Engine 🇮🇹

> **Futuristic cycling caption & telemetry engine for Strava & WhatsApp status updates.**  
> Inspired by [Bandók](https://bandok.com) witty ride naming, tailored for the **Basso Venta R** and the **Hyderabad Financial District Pelotón**.

---

## ⚡ Highlights & Features

- **Bandók Curation Engine:** Witty movie quotes, self-deprecating suffering, dry banter, and cycling philosophy inspired by Troy Hopwood's iconic [Bandók](https://bandok.com) Strava service.
- **Hyper-Personalized Context:**
  - **The Steed:** Built with pure Italian racing heritage for the **Basso Venta R** (carbon stiffness, Microtech wheels, aggressive aero cockpit).
  - **The Territory:** 4-days-a-week discipline through **Hyderabad's Financial District**—Kokapet Solar Roof Cycling Track, Waverock gradients, Durgam Cheruvu Cable Bridge, Knowledge City sprints, and post-ride Niloufer Irani Chai pitstops.
- **Top 1% Engineering Standards:**
  - **FastAPI + Pydantic v2**: Strict type safety, domain models, and automatic OpenAPI documentation (`/docs`).
  - **Dynamic Combinatorial Engine**: Seamlessly interpolates real ride metrics (km, km/h, elevation, suffer score, chai cups) into punchy captions.
  - **100% Test Coverage**: Complete Pytest test suite testing models, templates, telemetry formatters, and REST endpoints.
- **Futuristic Cyber-Aero UI:**
  - **Glassmorphic Cockpit:** Neon cyan accents (`#00f5d4`), Italian Tricolore details, carbon grid textures, and HUD corner brackets.
  - **Web Audio SFX:** Native browser audio synthesizer for telemetry chirps and laser clicks (no external audio files required, toggleable).
  - **Character Limit Gauges:** Real-time visual meters for Strava Title (<60 chars) and WhatsApp Status (<139 chars).
  - **1-Click Clipboard Formats:**
    - 📋 **Strava Title:** Snappy high-kudos punchline.
    - 📋 **Strava Full Activity Card:** Title + formatted telemetry + gear tags.
    - 📋 **WhatsApp Status:** Compact emoji-accented status text.
    - 💬 **WhatsApp Pelotón Broadcast:** Group chat formatted message with direct deep-link.
  - **🎨 Export HUD Social Card:** Generates a 1080x1080 hi-res dark cyberpunk telemetry image card in HTML5 Canvas for Instagram Story, WhatsApp Status, or Strava upload.
  - **Terminal CLI:** `python -m app.cli` for rapid command-line generation with automatic macOS clipboard copy (`pbcopy`).

---

## 🏗️ Architecture Overview

```
Vibe_proj_1/
├── app/
│   ├── config.py             # Settings, defaults, Hyderabad landmarks
│   ├── models/
│   │   └── quote.py          # Pydantic v2 domain schemas (Quote, Telemetry, Requests)
│   ├── data/
│   │   ├── quotes_db.py      # Curated Bandók & Pelotón quotes database
│   │   └── templates.py     # Dynamic telemetry interpolation templates
│   ├── services/
│   │   ├── generator.py      # Core generation & filtering engine
│   │   └── telemetry.py      # Formatting for Strava, WhatsApp & Canvas
│   ├── api/
│   │   └── routes.py         # REST API endpoints
│   ├── cli.py                # Terminal CLI with macOS clipboard integration
│   ├── main.py               # FastAPI application & static mounting
│   ├── static/
│   │   ├── css/futuristic.css# Cyberpunk/HUD styling & scanline overlays
│   │   └── js/
│   │       ├── sound.js      # Web Audio API synthesizer
│   │       ├── canvas_card.js# 1080x1080 Canvas graphic exporter
│   │       └── app.js        # Reactive SPA frontend logic
│   └── templates/
│       └── index.html        # Futuristic HUD single-page UI
├── tests/
│   ├── test_models.py        # Schema validation tests
│   ├── test_generator.py     # Generator & template tests
│   ├── test_telemetry_formatter.py # Formatting & truncation tests
│   └── test_api.py           # FastAPI endpoint tests
├── Dockerfile                # Production Docker container
├── docker-compose.yml        # Docker compose definition
├── requirements.txt          # Python dependencies
└── run.py                    # Server runner
```

---

## 🚀 Quickstart

### 1. Run the Web Application
```bash
# Start the server
python3 run.py
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser.

- **API Documentation (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 2. Run the Terminal CLI
For quick command-line access after a ride:
```bash
# Generate Hyderabad Financial District quote and copy to macOS clipboard
python3 -m app.cli --category hyd_fd_grit --km 42.5 --speed 32.8

# Generate Basso Venta R Aero quote formatted for WhatsApp Status
python3 -m app.cli --category basso_aero --format wa

# Generate full Strava activity description
python3 -m app.cli --format full --km 50 --elev 320 --loc "Kokapet Solar Track"
```

### 3. Run Test Suite
```bash
pytest -v
```

### 4. Deploy on Replit

The repo ships with a `.replit` config, so hosting needs no manual setup:

1. On [replit.com](https://replit.com), choose **Create Repl → Import from GitHub** and paste this repo's URL.
2. Press **Run**. The workflow installs `requirements.txt` and starts the server on port `5000`,
   which Replit proxies to the public `*.replit.dev` URL.
3. For an always-on public URL, open the **Deploy** tab and publish (`deploymentTarget = "autoscale"`
   is preconfigured).

`HOST` and `PORT` are read from the environment (`app/config.py`), so the same code runs locally on
`8000` and on Replit on `5000` with no edits. Autoreload only engages when `DEBUG=true`.

### 5. Docker Deployment
```bash
docker compose up --build
```

---

## 🧭 Vibe Categories Available

1. **Bandók Classic (`bandok_classic`)**: Movie quotes, Parks & Rec logic, dry wit, and philosophical road sarcasm.
2. **Hyderabad FD Grit (`hyd_fd_grit`)**: Kokapet Solar Track, Waverock gradients, Cable Bridge sunrises, Knowledge City sprints, and IT corridor survival.
3. **Basso Venta R Aero (`basso_aero`)**: Italian racing soul, Toray carbon stiffness, Microtech wheel hub acoustics, slammed stems.
4. **Pain Cave (`pain_cave`)**: Zone 4/5 threshold suffering, VO2 max, early alarms, and chasing kudos.
5. **Witty Sarcasm (`witty_sarcasm`)**: Justifying bike expenses, Strava sync ontology, aero diet delusions.
6. **Zen & Filosofia (`zen_filosofia`)**: Flow state, dawn stillness, tire hum, and mindfulness on two wheels.
7. **Chai Recovery (`chai_recovery`)**: Niloufer Irani Chai, Osmania biscuits, and post-ride caloric math.

---

## 📋 Keyboard Shortcuts

- **`Spacebar` or `R`**: Roll next quote (while outside form inputs).
- **Audio Toggle**: Click `🔊 SFX` in the top right to enable/mute high-tech audio synthesis.
