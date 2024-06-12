from sqlalchemy.exc import InternalError, OperationalError
from sqlalchemy import create_engine, text

from api.models.user import Base
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8"
APP_DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/userdb?charset=utf8"

engine = create_engine(APP_DB_URL, echo=True)


def database_exist():
    try:
        engine.connect()
        return True
    except (OperationalError, InternalError) as e:
        print(e)
        print("database does not exist.")
        return False


def create_database():
    if not database_exist():
        # appデータベースが存在しなければ作成
        root = create_engine(DB_URL, echo=True)
        with root.connect() as conn:
            conn.execute(text("CREATE DATABASE user"))
        print("created database.")
    Base.medadata.create_all(bind=engine)
    print("created tables.")


if __name__ == '__main__':
    create_database()
