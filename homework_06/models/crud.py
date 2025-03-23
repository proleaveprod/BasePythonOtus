from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from .models import Base, User
from .async_db import async_engine
from logger import logger as log

async def add( session: AsyncSession, instances: list):
    session.add_all(instances)
    await session.commit()
    return instances
        
async def get_users_with_posts(
    session: AsyncSession,
) -> list[User]:
    stmt = (
        # получить всех авторов
        select(User)
        # join for ORM
        .options(
            # to many -> selectinload
            selectinload(User.posts),
        )
        # всегда сортируем!
        .order_by(User.id)
    )
    users = (await session.scalars(stmt)).all()
    return list(users)
        
        
        
        
        
# Лень делать миграции для такого ДЗ. Удаляю и создаю заново БД, если требуется
async def create_database():
    log.info("Drop and Create of database...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    log.info("Drop and Create of database completed")