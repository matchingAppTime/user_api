from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class User(Base):
    __tablename__ = "USER_INFO"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cognito_id = Column(String(200))
    email = Column(String(200))
    nick_name = Column(String(30))
    sex = Column(Integer)
    birth = Column(Integer)
    ban_status = Column(Boolean)
