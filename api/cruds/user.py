from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List

import api.models.user as user_model
import api.schemas.user as user_schema


async def get_user(db: AsyncSession, user_id: int) -> Optional[user_schema.UserResponse]:
    """
    単一userのget

    :param db: db
    :param user_id: id
    :return: 単一ユーザー（Optional[user_model.User]）
    """
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user = result.scalars().first()

    return _mapping_user_response_schema(user)


async def search_users(db: AsyncSession, **kwargs) -> List[user_schema.UserResponse]:
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
    users = result.scalars().all()
    user_responses = [_mapping_user_response_schema(user) for user in users]
    return user_responses


async def search_users_by_keyword(db: AsyncSession, keyword: str) -> List[user_schema.UserResponse]:
    """
    自己紹介文に部分一致するユーザーを検索します。

    :param db: データベースセッション
    :param keyword: 検索キーワード
    :return: 部分一致するユーザーのリスト
    """
    query = select(user_model.User).where(user_model.User.about_me.like(f"%{keyword}%"))
    result: Result = await db.execute(query)
    users = result.scalars().all()
    user_responses = [_mapping_user_response_schema(user) for user in users]

    return user_responses


async def create_user(db: AsyncSession, user_create_schema: user_schema.UserCreate) -> user_schema.UserResponse:
    """
    ユーザーの作成

    :param db: db
    :param user_create_schema: リクエスト
    :return: 作成したユーザー
    """
    user_data = user_create_schema.model_dump()
    profile_data = user_data.pop("profile")
    attributes_data = user_data.pop("attributes")
    status_data = user_data.pop("status")

    new_user_data = {**profile_data, **attributes_data, **status_data}
    new_user_flatten = user_model.User(**new_user_data)
    db.add(new_user_flatten)
    await db.commit()
    await db.refresh(new_user_flatten)
    return _mapping_user_response_schema(new_user_flatten)


async def update_user(db: AsyncSession,
                      user_id: int,
                      user_update_schema: user_schema.UserUpdate) -> user_schema.UserResponse:
    """
    ユーザーの更新

    :param db: db
    :param user_id: id
    :param user_update_schema: リクエスト
    :return:
    """
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user = result.scalars().first()

    if user is None:
        return None

    user_data = user_update_schema.model_dump()
    profile_data = user_data.pop("profile")
    attributes_data = user_data.pop("attributes")
    status_data = user_data.pop("status")

    for key, value in {**profile_data, **attributes_data, **status_data}.items():
        setattr(user, key, value)

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return _mapping_user_response_schema(user)


async def delete_user(db: AsyncSession, user_id: int) -> user_schema.UserDeleteResponse:
    """
    ユーザーの削除
    :param db: db
    :param user_id: id
    :return: レスポンス
    """
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user = result.scalars().first()

    if user is None:
        return None

    await db.delete(user)
    await db.commit()
    return user_schema.UserDeleteResponse(id=user_id)


def _mapping_user_response_schema(user: user_model.User) -> user_schema.UserResponse:
    """
    DB形式のuserをschemasに変換
    :param user_model: DB形式のuser
    :return: schemasに合わせたuserResponse
    """
    user_data = user.__dict__

    # マッピング
    profile_data = {field: user_data[field] for field in user_schema.UserProfile.model_fields.keys()}
    attributes_data = {field: user_data[field] for field in user_schema.UserAttributes.model_fields.keys()}
    status_data = {field: user_data[field] for field in user_schema.UserStatus.model_fields.keys()}

    return user_schema.UserResponse(
        id=user_data["id"],
        profile=profile_data,
        attributes=attributes_data,
        status=status_data
    )
