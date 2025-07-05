from fastapi import APIRouter

from src.config.secrets import secrets

system_router = APIRouter(tags=["System"])


@system_router.get("/health")
async def health_check():
    """Perform a health check of the API."""
    return {"status": "ok"}


@system_router.get("/version")
async def get_version():
    """Return the current version of the application."""
    return {"version": secrets.VERSION}
