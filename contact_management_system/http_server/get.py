from ..db import queries as q
from ..db import db_connection
from .. import urls
import pprint


def fetch_contacts(cursor, user_id=None, contact_id=None, name=None, email=None):
    query = q.FETCH_CONTACTS
    if user_id or contact_id or name or email:
        where_values = []
        if user_id:
            where_values.append(f"user_id = '{user_id}'")
        if contact_id:
            where_values.append(f"contact_id = '{contact_id}'")
        elif name:
            where_values.append(f"name = '{name}'")
        elif email:
            where_values.append(f"email = '{email}'")
        query = query.replace(';', ' ') + "WHERE " + ' AND '.join(where_values) + ' ORDER BY contact_id;'

    cursor.execute(query)
    retrieved_contacts = cursor.fetchall()
    dict_result = {}
    for contact in retrieved_contacts:
        dict_result[contact['contact_id']] = {}
        dict_result[contact['contact_id']]['name'] = contact['name']
        dict_result[contact['contact_id']]['email'] = contact['email']

    # Attach numbers to contacts
    retrieved_contacts_ids = [contact['contact_id'] for contact in retrieved_contacts]
    for contact_id in retrieved_contacts_ids:
        # print(contact_id)
        cursor.execute(q.FETCH_NUMBERS, (contact_id,))
        retrieved_numbers = cursor.fetchall()
        for i, number in enumerate(retrieved_numbers, 1):
            dict_result[int(contact_id)][f"phone{i}"] = number['number']

    return dict_result


def get(url, query_data):
    if url == urls.CONTACT_PATH:
        try:
            with db_connection.Connect() as cur:
                return fetch_contacts(cur, **query_data)
        except TypeError as error:
            if "fetch_contacts() got an unexpected keyword argument" in str(error):
                return "Invalid Parameter"
