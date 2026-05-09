from celery import Celery

celery_app = Celery("brandintel", broker="redis://redis:6379/0")


@celery_app.task
def monitor_brand(brand: str) -> dict:
    return {"status": "queued", "brand": brand}
