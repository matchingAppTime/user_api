from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List

import api.models.user as user_model
import api.schemas.user as user_schema


async def get_user(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
    """
    単一userのget

    :param db: db
    :param user_id: id
    :return: 単一ユーザー（Optional[user_model.User]）
    """
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    return result.scalars().first()


async def search_users(db: AsyncSession, **kwargs) -> List[user_model.User]:
    """
    複数ユーザーの検索

    :param db: データベースセッション
    :param kwargs: 検索条件
    """
    query = select(user_model.User)

    conditions = []
    for key, value in kwargs.items():
        if value is not None:
            if hasattr(user_model.User, key):
                conditions.append(getattr(user_model.User, key) == value)

    if conditions:
        query = query.where(*conditions)

    result: Result = await db.execute(query)
    return result.scalars().all()


async def search_users_by_keyword(db: AsyncSession, keyword: str) -> List[user_model.User]:
    """
    自己紹介文に部分一致するユーザーを検索します。

    :param db: データベースセッション
    :param keyword: 検索キーワード
    :return: 部分一致するユーザーのリスト
    """
    query = select(user_model.User).where(user_model.User.about_me.like(f"%{keyword}%"))
    result: Result = await db.execute(query)
    return result.scalars().all()

async def create_user(db: AsyncSession, user_create_schema: user_schema.UserCreate) -> user_model.User:
    """
    ユーザーの作成

    :param db: db
    :param user_create_schema: リクエスト
    :return: 作成したユーザー
    """
    new_user = user_model.User(**user_create_schema.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

