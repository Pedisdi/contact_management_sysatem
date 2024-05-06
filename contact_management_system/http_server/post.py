from ..db import queries as q
from ..db import db_connection
from .. import urls


def add_contact(cursor, user_id, name, email="NULL", **numbers):
    cursor.execute(q.INSERT_QUERY_CONTACTS, (name, email, user_id))
    if numbers:
        query = q.FETCH_CONTACTS.replace(';', ' ') + f"WHERE email = '{email}';"
        cursor.execute(query)
        new_contact_id = cursor.fetchone()['contact_id']
        for number in numbers.values():
            cursor.execute(q.INSERT_QUERY_NUMBERS, (number, new_contact_id))
    return "The contact successfully added."


def delete_contact(cursor, user_id=None, contact_id=None, name=None, email=None, numbers=None):
    query = q.DELETE_CONTACT
    if user_id:
        pass


def post(url, form_data):
    if url == urls.ADD_CONTACT_PATH:
        with db_connection.Connect() as cur:
            return add_contact(cur, **form_data)
    elif url == urls.DELETE_CONTACT_PATH:
        with db_connection.Connect() as cur:
            delete_contact(cur, **form_data)

