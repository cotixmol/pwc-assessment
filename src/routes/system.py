from fastapi import APIRouter

from src.config.secrets import secrets

system_router = APIRouter()


@system_router.get("/health", tags=["System"])
async def health_check():
    """Perform a health check of the API."""
    return {"status": "ok"}


@system_router.get("/version", tags=["System"])
async def get_version():
    """Return the current version of the application."""
    return {"version": secrets.VERSION}
