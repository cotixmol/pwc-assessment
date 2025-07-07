import os
import sys
import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context
from dotenv import load_dotenv

# This ensures we can import from the project's source directory.
# This path should point to the root of your application source code.
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

# Import your models' Base metadata
# This is crucial for Alembic's autogenerate feature to detect model changes.
from src.models import Base, Harvest, Sale, Producer, Crop
from src.models.crop import CropType

# --- Environment Loading ---
# Get the project root directory to locate .env files
project_root = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
dotenv_local_path = os.path.join(project_root, '.env.local')
dotenv_path = os.path.join(project_root, '.env')

# Prioritize .env.local for local development overrides
if os.path.exists(dotenv_local_path):
    load_dotenv(dotenv_path=dotenv_local_path, override=True)
elif os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)

# --- Alembic Configuration ---
# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Set the SQLAlchemy URL from the loaded environment variable.
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("DATABASE_URL environment variable is not set or not loaded correctly.")
config.set_main_option("sqlalchemy.url", db_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for autogenerate support
target_metadata = Base.metadata

# --- Migration Functions ---

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """
    Helper function that is passed to run_sync.
    It configures the context and runs the migrations.
    """
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    # Create an async engine from the config
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool, # Use NullPool for single-use migration script
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


# --- Main Execution Logic ---
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
