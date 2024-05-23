from sqlalchemy import Column, Integer, String, Boolean, text
from api.db import Base


class User(Base):
    __tablename__ = "USER_INFO"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cognito_id = Column(String(200))
    email = Column(String(200))
    nick_name = Column(String(30))
    sex = Column(Integer, default=0, server_default=text("0"), nullable=False)
    birth = Column(Integer)
    area = Column(Integer, default=0, server_default=text("0"), nullable=False)
    income = Column(Integer, default=0, server_default=text("0"), nullable=False)
    height = Column(Integer, default=0, server_default=text("0"), nullable=False)
    body = Column(Integer, default=0, server_default=text("0"), nullable=False)
    about_me = Column(String(1000))
    prem_status = Column(Integer, default=0, server_default=text("0"), nullable=False)
    is_delete = Column(Integer, default=0, server_default=text("0"), nullable=False)
    penalty_status = Column(Integer, default=0, server_default=text("0"), nullable=False)
    free_point = Column(Integer, default=0, server_default=text("0"), nullable=False)
    paid_point = Column(Integer, default=0, server_default=text("0"), nullable=False)
    ban_status = Column(Boolean)
