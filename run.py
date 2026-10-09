"""Main runner script for AeroQuote / Bandók Engine."""
import uvicorn
from app.config import settings

if __name__ == "__main__":
    print(f"🚀 Starting {settings.APP_NAME} on http://localhost:{settings.PORT}")
    print("📍 Tailored for: Basso Venta R // Hyderabad Financial District Pelotón")
    print("📚 API Documentation: http://localhost:8000/docs")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
    )
