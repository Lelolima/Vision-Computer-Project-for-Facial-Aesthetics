"""
Teste de integração para a API
"""

import pytest
from fastapi.testclient import TestClient
from src.api.main import app


@pytest.fixture
def client():
    """Cria cliente de teste para a API."""
    return TestClient(app)


def test_health_check(client):
    """Testa endpoint de health check."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_ethics_disclosure(client):
    """Testa endpoint de divulgação ética."""
    response = client.get("/api/v1/ethics/disclosure?language=pt")
    assert response.status_code == 200
    data = response.json()
    assert "disclosure" in data
    assert "principles" in data


def test_analyze_missing_consent(client):
    """Testa que análise sem consentimento é recusada."""
    # Simular upload sem consentimento
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("test.jpg", b"fake image content", "image/jpeg")},
        data={"consent": "false"}
    )
    assert response.status_code == 400
    assert "consentimento" in response.json()["detail"].lower()


def test_analyze_invalid_file(client):
    """Testa que arquivo não-imagem é recused."""
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("test.txt", b"not an image", "text/plain")},
        data={"consent": "true"}
    )
    # Pode falhar na validação de content-type
    assert response.status_code in [400, 422]

def _png_bytes(color=(128, 128, 128)):
    import io
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (64, 64), color=color).save(buf, format="PNG")
    return buf.getvalue()


def test_analyze_without_face_returns_422_not_fake_scores(client):
    """Imagem sintética sem rosto não pode gerar pontuações fixas (antes: 500/AttributeError)."""
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("blank.png", _png_bytes(), "image/png")},
        data={"consent": "true"},
    )
    assert response.status_code == 422


def test_analyze_invalid_image_returns_400(client):
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("x.png", b"not an image", "image/png")},
        data={"consent": "true"},
    )
    assert response.status_code == 400


def test_analyze_requires_consent(client):
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("blank.png", _png_bytes(), "image/png")},
        data={"consent": "false"},
    )
    assert response.status_code == 400


def test_simulate_fallback_returns_image(client):
    response = client.post(
        "/api/v1/simulate",
        files={"file": ("blank.png", _png_bytes(), "image/png")},
        data={"procedure": "preenchimento_labial", "intensity": "0.5"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True and body["image_base64"]
