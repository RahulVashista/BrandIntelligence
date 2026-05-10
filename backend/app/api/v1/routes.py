from fastapi import APIRouter
from app.schemas.scan import ScanRequest, ScanResult
from app.schemas.brand import BrandCreate
from app.services.pipeline import run_scan_pipeline

router = APIRouter()

_SCANS: dict[str, ScanResult] = {}
_ALERTS: list[dict] = []
_BRANDS: list[dict] = []


@router.post('/scan', response_model=ScanResult)
async def scan(payload: ScanRequest) -> ScanResult:
    result = run_scan_pipeline(payload.url)
    _SCANS[result.scan_id] = result
    if result.risk_score >= 70:
        _ALERTS.append(result.model_dump())
    return result


@router.get('/scan/{scan_id}', response_model=ScanResult)
async def get_scan(scan_id: str) -> ScanResult:
    return _SCANS[scan_id]


@router.get('/alerts')
async def alerts() -> list[dict]:
    return _ALERTS


@router.get('/graph')
async def graph() -> dict:
    return {"nodes": [], "edges": []}


@router.post('/brand')
async def create_brand(payload: BrandCreate) -> dict:
    item = payload.model_dump()
    _BRANDS.append(item)
    return item


@router.post('/suppress')
async def suppress(payload: dict) -> dict:
    return {"status": "suppressed", "payload": payload}
