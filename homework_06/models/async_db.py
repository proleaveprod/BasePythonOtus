from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import db_url, db_echo

async_engine = create_async_engine(
    url = db_url,
    echo = db_echo
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)