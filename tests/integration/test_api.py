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