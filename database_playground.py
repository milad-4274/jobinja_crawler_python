from peewee import *

db = SqliteDatabase("jobinja.db")

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


db.connect()
db.create_tables([Person, Pet])


from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database
# Returns: 1

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database.
# Returns: 1

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')


grandma = Person.select().where(Person.name == 'Grandma L.').get()
print(grandma)

for person in Person.select():
    print(person.name)

# prints:
# Bob
# Grandma L.
# Herb

query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)

# prints:
# Kitty Bob
# Mittens Jr Herb

for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

# prints:
# Kitty
# Fido

############################# Sotinig

for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)

# prints:
# Fido
# Kitty
for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

# prints:
# Bob 1960-01-15
# Herb 1950-05-05
# Grandma L. 1935-03-01

####################### Combining filter expressions

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

for person in query:
    print(person.name, person.birthday)

# prints:
# Bob 1960-01-15
# Grandma L. 1935-03-01


################ Aggregates and Prefetch

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')

# prints:
# Bob 2 pets
# Grandma L. 0 pets
# Herb 1 pets