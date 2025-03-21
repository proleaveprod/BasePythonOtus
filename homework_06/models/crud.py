from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

async def create_user( session: AsyncSession, data: dict) -> User:
    user = User(**data)
    
    quit()
    session.add(user)
    await session.commit()
    return user