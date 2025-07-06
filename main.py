import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.db import engine
from src.config.logger import setup_logging
from src.routes import (
    crop_router,
    harvest_router,
    producer_router,
    sale_router,
    system_router,
)

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown.
    """
    logger.info("Application startup...")
    yield
    await engine.dispose()
    logger.info("Application shutdown and database connections closed.")


app = FastAPI(title="Pwc Assessment", lifespan=lifespan)

app.include_router(system_router)
app.include_router(harvest_router)
app.include_router(sale_router)
app.include_router(producer_router)
app.include_router(crop_router)
