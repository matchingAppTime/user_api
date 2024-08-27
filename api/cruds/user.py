from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from fastapi import HTTPException

import api.models.user as user_model
import api.schemas.user as user_schema
import api.repositories.db_operations as db_ops


async def get_user(db: AsyncSession, user_id: int) -> Optional[user_schema.UserResponse]:
    """
    単一userのget

    :param db: db
    :param user_id: id
    :return: 単一ユーザー（Optional[user_model.User]）
    """
    user = await db_ops.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="ユーザーが存在しません.")
    return _mapping_user_response_schema(user)


async def search_users(db: AsyncSession, **kwargs) -> List[user_schema.UserResponse]:
    """
    複数ユーザーの検索

    :param db: データベースセッション
    :param kwargs: 検索条件
    """
    conditions = []
    for key, value in kwargs.items():
        if value is not None:
            if hasattr(user_model.User, key):
                conditions.append(getattr(user_model.User, key) == value)

    users = await db_ops.search_users_by_conditions(db, conditions)
    return [_mapping_user_response_schema(user) for user in users]


async def search_users_by_keyword(db: AsyncSession, keyword: str) -> List[user_schema.UserResponse]:
    """
    自己紹介文に部分一致するユーザーを検索します。

    :param db: データベースセッション
    :param keyword: 検索キーワード
    :return: 部分一致するユーザーのリスト
    """
    users = await db_ops.search_users_by_keyword(db, keyword)
    return [_mapping_user_response_schema(user) for user in users]


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
    new_user = await db_ops.create_user_in_db(db, new_user_data)
    return _mapping_user_response_schema(new_user)

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
    user = await db_ops.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="ユーザーが存在しません.")

    user_data = user_update_schema.model_dump()
    profile_data = user_data.pop("profile")
    attributes_data = user_data.pop("attributes")
    status_data = user_data.pop("status")

    update_user_data = {**profile_data, **attributes_data, **status_data}

    updated_user = await db_ops.update_user_in_db(db, user, update_user_data)
    return _mapping_user_response_schema(updated_user)


async def delete_user(db: AsyncSession, user_id: int) -> user_schema.UserDeleteResponse:
    """
    ユーザーの削除
    :param db: db
    :param user_id: id
    :return: レスポンス
    """
    user = await db_ops.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="ユーザーが存在しません.")

    await db_ops.delete_user_in_db(db, user)
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
