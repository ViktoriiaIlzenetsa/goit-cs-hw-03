import logging
from psycopg2 import DatabaseError

from connect import create_connect

def create_db(conn):
    with open('create_tables.sql', 'r') as f:
        sql_stmt = f.read()
    c = conn.cursor()
    try:
        c.execute(sql_stmt)
        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    try:
        with create_connect() as conn:
            create_db(conn)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
    except DatabaseError as err:
        logging.error(f"Database error: {err}")

