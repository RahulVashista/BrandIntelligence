from urllib.parse import urlparse, parse_qs, urlunparse
from uuid import uuid4
from app.schemas.scan import ScanResult

SUSPICIOUS_KEYWORDS = {"login", "verify", "secure", "auth", "update"}
REDIRECT_KEYS = {"url", "redirect", "next", "return", "target"}


def canonicalize(url: str) -> tuple[str, dict]:
    parsed = urlparse(url)
    host = (parsed.hostname or "").encode("idna").decode("ascii")
    path = parsed.path or "/"
    canon = urlunparse((parsed.scheme.lower(), host, path, "", parsed.query, ""))
    return canon, {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "path": parsed.path,
        "query": parsed.query,
        "fragment": parsed.fragment,
        "port": parsed.port,
    }


def run_scan_pipeline(url: str) -> ScanResult:
    canonical_url, anatomy = canonicalize(url)
    query = parse_qs(anatomy["query"])
    reasons: list[str] = []
    score = 0

    lower_path = (anatomy["path"] or "").lower()
    if any(k in lower_path for k in SUSPICIOUS_KEYWORDS):
        reasons.append("suspicious_path_keywords")
        score += 25

    if any(k in query for k in REDIRECT_KEYS):
        reasons.append("redirect_parameter_present")
        score += 30

    host = (anatomy["host"] or "").lower()
    if host.count(".") >= 3:
        reasons.append("deep_subdomain_structure")
        score += 15

    if "xn--" in canonical_url:
        reasons.append("idn_punycode_detected")
        score += 25

    score = min(score, 100)
    verdict = "likely_phishing" if score >= 70 else "suspicious" if score >= 40 else "low_risk"

    return ScanResult(
        scan_id=str(uuid4()),
        original_url=url,
        canonical_url=canonical_url,
        risk_score=score,
        verdict=verdict,
        confidence=round(min(0.5 + score / 200, 0.99), 2),
        reason_codes=reasons,
        evidence={"url_anatomy": anatomy, "query_params": query},
    )
