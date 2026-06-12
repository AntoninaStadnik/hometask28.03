import os

import dotenv
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

# host = "localhost"
# port = 5432
# user = "postgres"
# password = "password"
# db = "academy"


dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")


print(db)

db_uri = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables
print(list(tables.keys()))

# вивести інформацію про всі навчальні групи
# query = f"""
#     SELECT *
#     FROM groups
#
# """
#
# #  підправити текст
# query = text(query)
#
# # запуск
# result = session.execute(query)
#
# # виведення результатів(рядків)
# for row in result:
#     print(row)

# вивести інформацію про всіх викладачів
# query = f"""
#     SELECT *
#     FROM teachers
#
# """
#
# #  підправити текст
# query = text(query)
#
# # запуск
# result = session.execute(query)
#
# # виведення результатів(рядків)
# for row in result:
#     print(row)

# вивести назви кафедр і груп, які до них відносяться

query = f"""
    SELECT d.name, g.name
    FROM departments d join groups g on d.id = g.departmentid

"""

#  підправити текст
query = text(query)

# запуск
result = session.execute(query)

# виведення результатів(рядків)
for row in result:
    print(row)
