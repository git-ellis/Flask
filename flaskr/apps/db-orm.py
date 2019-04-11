from flask import Flask
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from flask_sqlalchemy import SQLAlchemy

DB_FILES = 'constant/db/database.db'
app = Flask(__name__)

# 核心介面，封裝了對db所有的操作(DBAPI)，echo -- python standard logging
engine = create_engine("sqlite:///" + DB_FILES, echo=True)
# engine.connect() - establishes a real DBAPI connection to the database
# 通常不用這個方法，ORM會在幕後調用這方法

Session = sessionmaker(bind=engine)

# 聲明基底類別，負責維護物件與Table之間的對映關係(目錄)
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100))
    password = Column("password", String(100))
    email = Column("email", String(100))


def find_all():
    result_ls = []
    session = Session()

    datas = session.query(User).all()
    for user in datas:
        ud = dict()
        ud['id'] = user.id
        ud['name'] = user.name
        ud['password'] = user.password
        ud['email'] = user.email
        result_ls.append(ud)

    session.close()

    return result_ls


def create(user):
    new_user = User(name=user["name"],
                    password=user["password"],
                    email=user["email"])

    session = Session()
    session.add(new_user)
    session.commit()
    session.close


def delete(id):
    session = Session()

    # 查詢待刪除的用戶
    user = session.query(User).filter_by(id=id).one()
    session.delete(user)
    session.commit()
    session.close()


def update(user):
    session = Session()



if __name__ == "__main__":
    # user = dict()
    # user['name'] = "Ellis"
    # user['password'] = '12321'
    # user['email'] = "ellis123@gmail.com"
    #
    # create(user)

    delete(4)

    # 建立資料庫的table
    # Base.metadata.create_all(engine)
