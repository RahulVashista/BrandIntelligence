from fastapi.testclient import TestClient
from app.main import app


def test_scan_endpoint() -> None:
    client = TestClient(app)
    resp = client.post('/v1/scan', json={"url": "https://example.com/login?url=https://a.co"})
    assert resp.status_code == 200
    assert "risk_score" in resp.json()
