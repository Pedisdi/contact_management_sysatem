# def fetch_contacts(cursor, user_id=None, contact_id=None, name=None, email=None):
#     query = q.FETCH_CONTACTS
#     if user_id or contact_id or name or email:
#         query = query.replace(';', ' ') + "WHERE "
#         if user_id:
#             query += f"user_id = '{user_id}'"
#     print(query)
#     cursor.execute(query)
#     retrieved_records = cursor.fetchall()
#     return retrieved_records




# with db_connection.Connect() as cur:
# pprint.pprint(fetch_contacts(cur, user_id=4, email='erica23@example.net'))
# pprint.pprint(fetch_contacts(cur))
# print(fetch_contacts(cur)[0]['name'])



# FETCH_CONTACTS = "SELECT c.name, c.email, n.number FROM contacts c INNER JOIN numbers n USING(contact_id);"
# FETCH_CONTACTS = "SELECT * FROM users"



# Auto Value Insertion
def insert(table_name, **field_value):
    print(field_value.values())
    query = f"INSERT INTO {table_name} "
    fields = "("
    values = "VALUES ("
    for field, value in field_value.items():
        fields += f"{field}, "
        values += f"'{value}', "
    fields = fields.strip(', ')
    values = values.strip(', ')

    fields += ") "
    values += ");"
    query += fields + values
    print(query)

