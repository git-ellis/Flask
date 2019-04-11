from flask import Flask
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

DB_FILES = 'constant/db/database.db'
app = Flask(__name__)
engine = create_engine("sqlite:///" + DB_FILES, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100))
    password = Column("password", String(100))
    email = Column("email", String(100))


def find_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    print(Session, session)

    list = session.query(User).all()

    result_ls = []
    for user in list:
        ud = dict()
        ud['id'] = user.id
        ud['name'] = user.name
        ud['password'] = user.password
        ud['email'] = user.email
        result_ls.append(ud)

    session.close()

    return result_ls


if __name__ == "__main__":
    print(find_all())
    # 建立資料庫的table
    # Base.metadata.create_all(engine)

# def find_all():
#     conn = get_connection()
#     curs = conn.cursor()
#     curs.execute("SELECT * FROM USER")
#     reset_set = curs.fetchall()
#     print(reset_set)
#
#     user_list = []
#     for row in reset_set:
#         user = dict()
#         user['id'] = row[0]
#         user['name'] = row[1]
#         user['password'] = row[2]
#         user['email'] = row[3]
#         user_list.append(user)
#
#     print(f"user_list = {user_list}")
#     conn.close()
#
#
# def create(name, password, email):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         sql = "INSERT INTO USER(NAME, PASSWORD, EMAIL) VALUES(?, ?, ?)"
#         r = cursor.execute(sql, [name, password, email])
#
#         print(r)
#         print("cursor.rowcount =", cursor.rowcount)
#         print("cursor.lastrowid =", cursor.lastrowid)
#
#         conn.commit()
#     except Exception as e:
#         traceback.print_exc()
#         print("creation failed")
#         conn.rollback()
#     finally:
#         conn.close()
#
#
# def delete(id):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         sql = "DELETE FROM USER WHERE ID = ?"
#         r = cursor.execute(sql, [id])
#
#         print(r)
#         print("cursor.rowcount =", cursor.rowcount)
#         print("cursor.lastrowid =", cursor.lastrowid)
#
#         conn.commit()
#     except:
#         print("deletion failed")
#         conn.rollback()
#     finally:
#         conn.close()
#
#
# def update(id, name, password, email):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         sql = "UPDATE USER SET NAME = ?, PASSWORD = ?, EMAIL = ? WHERE ID = ?"
#         r = cursor.execute(sql, [name, password, email, id])
#
#         print(r)
#         print("cursor.rowcount =", cursor.rowcount)
#         print("cursor.lastrowid =", cursor.lastrowid)
#
#         conn.commit()
#     except:
#         print("update failed")
#         conn.rollback()
#     finally:
#         conn.close()
