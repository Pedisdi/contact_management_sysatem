import psycopg2
from psycopg2 import extras
from .db_config import load_db_config


class Connect:

    def __init__(self):
        self.config = load_db_config()
        # print(self.config)
        self.conn = None
        self.cur = None

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**self.config)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        except psycopg2.DatabaseError:
            print("DataBaseError!")
            raise
        else:
            return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()


