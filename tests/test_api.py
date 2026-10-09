"""Integration tests for FastAPI endpoints."""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "version" in data


def test_serve_html_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "AERO" in response.text
    assert "Basso Venta R" in response.text


def test_api_categories_endpoint():
    response = client.get("/api/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert len(data["categories"]) > 0


def test_api_landmarks_endpoint():
    response = client.get("/api/landmarks")
    assert response.status_code == 200
    landmarks = response.json()
    assert isinstance(landmarks, list)
    assert any("Kokapet" in l for l in landmarks)


def test_api_generate_endpoint_default():
    payload = {
        "telemetry": {
            "distance_km": 42.0,
            "avg_speed_kph": 31.0,
            "elevation_m": 220,
            "location": "Kokapet Solar Roof",
            "bike": "Basso Venta R"
        }
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "primary" in data
    assert "alternatives" in data
    assert data["primary"]["strava_title"] != ""
    assert data["primary"]["whatsapp_status"] != ""


def test_api_random_endpoint():
    response = client.get("/api/random?category=hyd_fd_grit")
    assert response.status_code == 200
    quote = response.json()
    assert quote["category"] == "hyd_fd_grit"
    assert len(quote["headline"]) > 0


def test_api_custom_quote_lifecycle():
    payload = {
        "headline": "Testing the Basso on Hyderabad hills",
        "subtext": "Fast descent into Financial District",
        "category": "basso_aero",
        "tags": ["test", "basso"]
    }
    response = client.post("/api/quotes/custom", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["headline"] == payload["headline"]
    assert data["category"] == "basso_aero"
