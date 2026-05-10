# BrandIntelligence

Analyst-grade phishing and brand impersonation intelligence platform.

## Stack
- Backend: FastAPI + SQLAlchemy + Pydantic
- Queue: Celery + Redis
- DB: PostgreSQL
- Object storage: MinIO
- Frontend: React (Vite)

## Quick start

Recommended:

```bash
./run-kali.sh
```

Services:
- Frontend: http://localhost:5173
- API docs: http://localhost:8000/docs
- MinIO console: http://localhost:9001

## Validation checks

```bash
docker ps
curl http://localhost:8000/health
curl http://localhost:5173
```

Expected:
- API health returns `{"status":"ok"}`.
- Frontend returns HTML containing the Vite root page.
- `docker ps` shows `api`, `worker`, `redis`, `postgres`, `minio`, and `frontend`.
