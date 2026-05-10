from pydantic import BaseModel, HttpUrl
from typing import Any

class ScanRequest(BaseModel):
    url: HttpUrl


class ScanResult(BaseModel):
    scan_id: str
    original_url: str
    canonical_url: str
    risk_score: int
    verdict: str
    confidence: float
    reason_codes: list[str]
    evidence: dict[str, Any]
