from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.user as user_schema
import api.cruds.user as user_cruds
from api.db import get_db
router = APIRouter()


@router.get("/users", response_model=List[user_schema.UserBase])
async def search_users(
        cognito_id: str = Query(None),
        email: str = Query(None),
        nick_name: str = Query(None),
        sex: int = Query(None),
        birth: int = Query(None),
        area: int = Query(None),
        income: int = Query(None),
        height: int = Query(None),
        body: int = Query(None),
        prem_status: int = Query(None),
        is_delete: int = Query(None),
        penalty_status: int = Query(None),
        free_point: int = Query(None),
        paid_point: int = Query(None),
        ban_status: bool = Query(None),
        db: AsyncSession = Depends(get_db)
):
    return await user_cruds.search_users(
        db=db,
        cognito_id=cognito_id,
        email=email,
        nick_name=nick_name,
        sex=sex,
        birth=birth,
        area=area,
        income=income,
        height=height,
        body=body,
        prem_status=prem_status,
        is_delete=is_delete,
        penalty_status=penalty_status,
        free_point=free_point,
        paid_point=paid_point,
        ban_status=ban_status
    )


@router.get("/users/search", response_model=List[user_schema.UserBase])
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
    if user is None:
        raise HTTPException(status_code=404, detail="ユーザーが存在しません.")
    return user


@router.post("/user", response_model=user_schema.UserCreateResponse)
async def create_user(body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    created_user_response = await user_cruds.create_user(db=db, user_create_schema=body)
    return created_user_response


@router.put("/user/{user_id}")
async def update_user(user_id: int):
    return f"ユーザーをアップデートしました {user_id}"


@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    return f"ユーザーを削除しました {user_id}"
