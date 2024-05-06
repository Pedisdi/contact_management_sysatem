from .db_connection import Connect
import psycopg2
from psycopg2 import extras


# Drop Tables
DROP_TABLE_USERS = "DROP TABLE users;"
DROP_TABLE_CONTACTS = "DROP TABLE contacts;"
DROP_TABLE_NUMBERS = "DROP TABLE numbers;"

CREATE_TABLE_USERS = ("CREATE TABLE IF NOT EXISTS users ("
                      "user_id SERIAL PRIMARY KEY,"
                      "username VARCHAR(100) UNIQUE,"
                      "password VARCHAR(100)"
                      ");")

# Create Tables
CREATE_TABLE_CONTACTS = ("CREATE TABLE IF NOT EXISTS contacts ("
                         "contact_id SERIAL PRIMARY KEY,"
                         "name VARCHAR(50),"
                         "email VARCHAR(50),"
                         "user_id INT,"
                         "FOREIGN KEY (user_id) REFERENCES users(user_id)"
                         ");")

CREATE_TABLE_NUMBERS = ("CREATE TABLE IF NOT EXISTS numbers ("
                        "number_id SERIAL PRIMARY KEY,"
                        "number VARCHAR(50),"
                        "contact_id INT,"
                        "FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)"
                        ");")

# Insert VALUES
INSERT_QUERY_USER = "INSERT INTO users(username, password) VALUES (%s, %s);"
INSERT_QUERY_CONTACTS = "INSERT INTO contacts(name, email, user_id) VALUES (%s, %s, %s);"
INSERT_QUERY_NUMBERS = "INSERT INTO numbers(number, contact_id) VALUES (%s, %s);"

# Fetch Record
FETCH_CONTACTS = "SELECT contact_id, name, email FROM contacts;"
FETCH_NUMBERS = "SELECT number FROM numbers WHERE contact_id = %s;"
FETCH_CONTACTS = "SELECT c.name, c.email, n.number FROM contacts c INNER JOIN numbers n USING(contact_id);"

# Delete Record
DELETE_CONTACT = "DELETE FROM contacts WHERE "


if __name__ == '__main__':
    # with psycopg2.connect(password="88493144", user="postgres", port="8432", database="contact_management_system", host="localhost" ).cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    with Connect() as cur:
        cur.execute(FETCH_CONTACTS)
        res = cur.fetchall()
        print(res)
        print(res[0])
        print(res[0]['name'])
        # rr = cur.fetchone()
        # print(cur.fetchone())
        # print(rr)
        # print(rr['name'])
