from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    id: int
    cognito_id: Optional[str] = Field(None, example="jrigjeriopjoioijojie")
    email: Optional[str] = Field(None, example="xxx@mail.com")
    nick_name: Optional[str] = Field(None, example="umemiya")
    sex: Optional[int] = Field(0, example=1)
    birth: Optional[int] = Field(None, example=19950102)
    ban_status: bool = Field(False, example=False)


class UserCreate(BaseModel):
    cognito_id: Optional[str] = Field(None, example="jrigjeriopjoioijojie")
    email: Optional[str] = Field(None, example="xxx@mail.com")
    nick_name: Optional[str] = Field(None, example="umemiya")
    sex: Optional[int] = Field(2, example=1)
    birth: Optional[int] = Field(None, example=19950102)
    ban_status: bool = Field(False, example=False)

    class Config:
        orm_mode = True


class UserCreateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    cognito_id: Optional[str] = Field(None, example="jrigjeriopjoioijojie")
    email: Optional[str] = Field(None, example="xxx@mail.com")
    nick_name: Optional[str] = Field(None, example="umemiya")
    sex: Optional[int] = Field(2, example=1)
    birth: Optional[int] = Field(None, example=19950102)
    ban_status: bool = Field(False, example=False)

    class Config:
        orm_mode = True