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
        ban_status: bool = Query(None),
        db: AsyncSession = Depends(get_db)
):
    return await user_cruds.search_users(
        db=db,
        cognito_id=cognito_id,
        email=email,
        nick_name=nick_name,
        sex=sex,
        ban_status=ban_status
    )



@router.get("/user/{user_id}", response_model=user_schema.UserBase)
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
