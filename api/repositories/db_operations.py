from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from typing import Optional, List

import api.models.user as user_model


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    return result.scalars().first()


async def search_users_by_conditions(db: AsyncSession, conditions: List) -> List[user_model.User]:
    query = select(user_model.User).where(*conditions)
    result: Result = await db.execute(query)
    return result.scalars().all()


async def search_users_by_keyword(db: AsyncSession, keyword: str) -> List[user_model.User]:
    query = select(user_model.User).where(user_model.User.about_me.like(f"%{keyword}%"))
    result: Result = await db.execute(query)
    return result.scalars().all()


async def create_user_in_db(db: AsyncSession, user_data: dict) -> user_model.User:
    new_user = user_model.User(**user_data)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def update_user_in_db(db: AsyncSession, user: user_model.User, updated_data: dict) -> user_model.User:
    for key, value in updated_data.items():
        setattr(user, key, value)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user_in_db(db: AsyncSession, user: user_model.User) -> None:
    await db.delete(user)
    await db.commit()
