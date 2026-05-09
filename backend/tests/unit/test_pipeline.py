from app.services.pipeline import run_scan_pipeline


def test_detects_redirect_and_keywords() -> None:
    result = run_scan_pipeline("https://secure-login.example.com/auth/update?redirect=https://evil.com")
    assert result.risk_score >= 40
    assert "redirect_parameter_present" in result.reason_codes
