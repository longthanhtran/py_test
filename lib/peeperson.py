from peewee import *
from faker import Factory

fake = Factory.create()

mysql_db = MySQLDatabase(
    'pydb',
    host   = '192.168.10.51',
    user   = 'tt1',
    passwd ='helloworld')

class BaseModel(Model):
    """ A base class that uses MySQL database"""
    class Meta:
        database = mysql_db

class Person(BaseModel):
    name        = CharField()
    email       = CharField()
    birthday    = DateField(null = True)
    is_relative = BooleanField()

Person.create_table(fail_silently=True)

person_a = []
for i in range(1,10000):
    person_a.append({
            'name' : fake.name(),
            'email' : fake.email(),
            'birthday' : fake.date(),
            'is_relative' : fake.boolean()}
    )

with mysql_db.atomic():
    Person.insert_many(person_a).execute()

# mysql_db.connect()
# mysql_db.create_tables([Person])