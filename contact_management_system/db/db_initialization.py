import faker as f
import random
from . import queries as q
from .db_connection import Connect


def drop_tables(cur):
    cur.execute(q.DROP_TABLE_NUMBERS)
    cur.execute(q.DROP_TABLE_CONTACTS)
    cur.execute(q.DROP_TABLE_USERS)


def create_tables(cur):
    cur.execute(q.CREATE_TABLE_USERS)
    cur.execute(q.CREATE_TABLE_CONTACTS)
    cur.execute(q.CREATE_TABLE_NUMBERS)


def insert_values(cur, users_qty=10, contact_qty=40, numbers_qty=80):
    fake = f.Faker()
    values = []
    for _ in range(users_qty):
        username = fake.user_name()
        password = fake.password()
        values.append([username, password])
    cur.executemany(q.INSERT_QUERY_USER, values)

    values = []
    for _ in range(contact_qty):
        user_id = random.randint(1, users_qty)
        name = fake.name()
        email = fake.email()
        values.append([name, email, user_id])
    cur.executemany(q.INSERT_QUERY_CONTACTS, values)

    values = []
    for _ in range(numbers_qty):
        contact_id = random.randint(1, contact_qty)
        number = fake.phone_number()
        values.append([number, contact_id])
    cur.executemany(q.INSERT_QUERY_NUMBERS, values)


with Connect() as cursor:
    drop_tables(cursor)
    create_tables(cursor)
    insert_values(cursor)
