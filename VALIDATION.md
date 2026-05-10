# Validation Matrix

| Feature | Test | Operational Validation |
|---|---|---|
| URL normalization and anatomy parsing | `backend/tests/unit/test_pipeline.py` | POST `/v1/scan` with encoded/IDN URLs |
| Risk scoring engine | `backend/tests/unit/test_pipeline.py` | Verify reason codes + score bucket in API response |
| REST API endpoints | `backend/tests/integration/test_api.py` | Open `/docs` and invoke `/v1/scan`, `/v1/alerts` |
| CLI | manual | `python cli/brandintel.py scan <url>` |
| Docker deployment | manual | `./run-kali.sh` |
| Container health checks | manual | `docker ps`, `curl http://localhost:8000/health`, `curl http://localhost:5173` |
