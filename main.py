import logging
from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from src.config import db
from src.config.logger import setup_logging
from src.config.secrets import secrets
from src.routes import system_router

setup_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup...")

    logger.info("Attempting to connect to the database...")
    db.db_pool = await asyncpg.create_pool(
        dsn=secrets.DATABASE_URL, min_size=5, max_size=20
    )
    logger.info("Database connection pool created and seeded successfully.")

    yield

    if db.db_pool:
        await db.db_pool.close()
        logger.info("Database connection pool closed.")


app = FastAPI(title="Pwc Assessment", lifespan=lifespan)
app.include_router(system_router)
