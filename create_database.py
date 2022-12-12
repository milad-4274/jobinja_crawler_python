from peewee import *
from Models import *

db = SqliteDatabase("jobinja.db")

db.connect()
db.create_tables([Job,Skill,JobSkill])

# print(db.get_tables())
# print(db.ge.get_columns())