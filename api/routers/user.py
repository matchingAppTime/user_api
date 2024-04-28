from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.user as user_schema
import api.cruds.user as user_cruds
from api.db import get_db
router = APIRouter()


@router.get("/users", response_model=List[user_schema.UserBase])
async def get_users():
    return {"user1": "aaaa", "user2": "bbbb"}


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
