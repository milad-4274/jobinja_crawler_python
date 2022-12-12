from peewee import *
from Models import *

db = SqliteDatabase("jobinja.db")

db.create_tables([Job,Skill,JobSkill])