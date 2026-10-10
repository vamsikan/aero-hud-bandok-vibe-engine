"""Main runner script for AeroQuote / Bandók Engine."""
import uvicorn

from app.config import settings

if __name__ == "__main__":
    print(f"🚀 Starting {settings.APP_NAME} on http://{settings.HOST}:{settings.PORT}")
    print("📍 Tailored for: Basso Venta R // Hyderabad Financial District Pelotón")
    print(f"📚 API Documentation: http://{settings.HOST}:{settings.PORT}/docs")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        # Autoreload is a local-development convenience only; hosted runs stay stable.
        reload=settings.DEBUG,
    )
