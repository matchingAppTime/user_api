from pydantic import BaseModel, Field
from typing import Optional


class UserProfile(BaseModel):
    """
    ユーザーのプロフィール情報
    """
    cognito_id: Optional[str] = Field(None, example="jrigjeriopjoioijojie")
    email: Optional[str] = Field(None, example="xxx@mail.com")
    nick_name: Optional[str] = Field(None, example="umemiya")
    about_me: Optional[str] = Field(None, example="こんにちは！umemiyaです！")


class UserAttributes(BaseModel):
    """
    ユーザーの特徴情報
    """
    sex: Optional[int] = Field(0, example=1)
    birth: Optional[int] = Field(None, example=19950102)
    area: Optional[int] = Field(0, example=47)
    income: Optional[int] = Field(0, example=2)
    height: Optional[int] = Field(0, example=165)
    body: Optional[int] = Field(0, example=3, description="1~7")


class UserStatus(BaseModel):
    """
    ユーザーのアプリ内ステータス
    """
    prem_status: bool = Field(False, example=True)
    is_delete: bool = Field(False, example=False)
    penalty_status: Optional[int] = Field(0, example=0)
    free_point: Optional[int] = Field(0, example=0)
    paid_point: Optional[int] = Field(0, example=0)
    ban_status: bool = Field(False, example=False)


class UserBase(BaseModel):
    profile: UserProfile
    attributes: UserAttributes
    status: UserStatus

    class Config:
        orm_mode = True
        from_attributes = True


class UserSearchRequest(BaseModel):
    cognito_id: Optional[str] = None
    email: Optional[str] = None
    nick_name: Optional[str] = None
    sex: Optional[int] = None
    birth: Optional[int] = None
    area: Optional[int] = None
    income: Optional[int] = None
    height: Optional[int] = None
    body: Optional[int] = None
    prem_status: Optional[int] = None
    is_delete: Optional[int] = None
    penalty_status: Optional[int] = None
    free_point: Optional[int] = None
    paid_point: Optional[int] = None
    ban_status: Optional[bool] = None


class UserCreate(UserBase):
    # cognitoのIDトークン
    idToken: str

    class Config:
        orm_mode = True
        from_attributes = True


class UserCreateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class UserUpdate(UserBase):
    pass


class UserDeleteResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

