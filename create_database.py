from peewee import *
from Models import *

db = SqliteDatabase("./jobinja.db")

db.connect()
db.create_tables([Job,Skill,JobSkill])
db.close()