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


async def search_users(
        db: AsyncSession,
        cognito_id: Optional[str] = None,
        email: Optional[str] = None,
        nick_name: Optional[str] = None,
        sex: Optional[int] = None,
        ban_status: Optional[bool] = None
) -> List[user_model.User]:
    """
    複数ユーザーの検索

    :param db: データベースセッション
    :param cognito_id: Cognito ID
    :param email: メールアドレス
    :param nick_name: ニックネーム
    :param sex: 性別
    :param ban_status: バン状態
    """
    query = select(user_model.User)
    if cognito_id is not None:
        query = query.where(user_model.User.cognito_id == cognito_id)
    if email is not None:
        query = query.where(user_model.User.email == email)
    if nick_name is not None:
        query = query.where(user_model.User.nick_name == nick_name)
    if sex is not None:
        query = query.where(user_model.User.sex == sex)
    if ban_status is not None:
        query = query.where(user_model.User.ban_status == ban_status)

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

