from datetime import datetime

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

from config.database_config import DATABASE_URL
from models import *

load_dotenv()

config = context.config
config.set_main_option(
    name="sqlalchemy.url",
    value=DATABASE_URL
)


def get_migration_filename(message):
    date_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return f"{date_str}_{message}.py"


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=SQLModel.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=SQLModel.metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()

else:
    run_migrations_online()
