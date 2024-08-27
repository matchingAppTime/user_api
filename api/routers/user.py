from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.user as user_schema
import api.cruds.user as user_cruds
from api.db import get_db

router = APIRouter()


@router.get("/")
async def health_check():
    return "OK."


@router.get("/users", response_model=List[user_schema.UserResponse])
async def search_users(
        query: user_schema.UserSearchRequest = Depends(),
        db: AsyncSession = Depends(get_db)
):
    return await user_cruds.search_users(
        db=db,
        **query.model_dump(exclude_unset=True)
    )


@router.get("/users/search", response_model=List[user_schema.UserResponse])
async def search_users_by_keyword_route(
        keyword: str = Query(..., description="検索キーワード"),
        db: AsyncSession = Depends(get_db)
    ) -> List[user_schema.UserBase]:
    """
    自己紹介文に部分一致するユーザーを検索します
    """
    return await user_cruds.search_users_by_keyword(db=db, keyword=keyword)


@router.get("/user/{user_id}", response_model=user_schema.UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_cruds.get_user(db=db, user_id=user_id)
    return user


@router.post("/user", response_model=user_schema.UserCreateResponse)
async def create_user(
        body: user_schema.UserCreate,
        db: AsyncSession = Depends(get_db),
):
    created_user_response = await user_cruds.create_user(db=db, user_create_schema=body)
    return created_user_response


@router.put("/user/{user_id}")
async def update_user(
        user_id: int,
        body: user_schema.UserUpdate,
        db: AsyncSession = Depends(get_db),
):
    updated_user_response = await user_cruds.update_user(db=db, user_id=user_id, user_update_schema=body)
    return updated_user_response


@router.delete("/user/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted_user_response = await user_cruds.delete_user(db=db, user_id=user_id)
    return deleted_user_response
