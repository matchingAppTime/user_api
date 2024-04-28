from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/users")
async def get_users():
    return {"user1": "aaaa", "user2": "bbbb"}


@router.get("/user/{user_id}")
async def get_user(user_id: int):
    return {f"user{user_id}": "xxxx"}


@router.post("/user")
async def create_user():
    return "ユーザーを作成しました"


@router.put("/user/{user_id}")
async def update_user(user_id: int):
    return f"ユーザーをアップデートしました {user_id}"


@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    return f"ユーザーを削除しました {user_id}"
