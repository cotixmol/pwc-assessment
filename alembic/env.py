import os
import sys
import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# This ensures we can import from the 'src' directory.
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Base, Producer, Crop, Harvest, Sale

# Get the project root directory
project_root = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

dotenv_local_path = os.path.join(project_root, '.env.local')
dotenv_path = os.path.join(project_root, '.env')

if os.path.exists(dotenv_local_path):
    print("INFO: Loading environment from .env.local")
    load_dotenv(dotenv_path=dotenv_local_path, override=True)
# Otherwise, load the standard .env file for other environments (like Docker).
elif os.path.exists(dotenv_path):
    print("INFO: Loading environment from .env")
    load_dotenv(dotenv_path=dotenv_path)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Set the SQLAlchemy URL from the loaded environment variable.
# REMOVE the hardcoded string replacement.
db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise ValueError("DATABASE_URL environment variable is not set.")
config.set_main_option("sqlalchemy.url", db_url)

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for autogenerate support
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
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
    Helper function to run the migrations within a transaction.
    """
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    This requires creating an Engine and associating a
    connection with the context.
    """
    from src.config.db import engine

    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await engine.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
