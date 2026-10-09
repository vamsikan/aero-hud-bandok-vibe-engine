"""FastAPI application initialization and routing."""
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.routes import router as api_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Futuristic Strava & WhatsApp cycling caption generator inspired by Bandók (bandok.com), crafted for Basso Venta R riders in Hyderabad.",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static & template mounts
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Register API routes
app.include_router(api_router)


@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    """Serve the futuristic telemetry HUD single-page application."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.APP_NAME,
            "version": settings.VERSION,
            "default_bike": settings.DEFAULT_BIKE,
            "default_location": settings.DEFAULT_LOCATION,
            "landmarks": settings.HYD_LOCATIONS,
        }
    )


@app.get("/health")
async def health_check():
    """Service health probe."""
    return {"status": "operational", "app": settings.APP_NAME, "version": settings.VERSION}
