import logging
from faker import Faker
from random import randint
from psycopg2 import DatabaseError

from connect import create_connect

fake = Faker("uk_UA")
TASK_COUNT = 1000
STATUS_COUNT = 3
USERS_COUNT = 100


def insert_data(conn):
    sql_stmt_tasks = """
    INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)
    """
    sql_stmt_status = """
    INSERT INTO status (name) VALUES (%s)
    """
    STATUS_TYPES = [('new',), ('in progress',), ('completed',)]

    sql_stmt_users = """
    INSERT INTO users (fullname, email) VALUES (%s, %s)
    """

    c = conn.cursor()
    try:
        c.executemany(sql_stmt_status, STATUS_TYPES)
        
        for _ in range(USERS_COUNT):
            fullname = fake.name()
            email = fake.email()
            c.execute(sql_stmt_users, (fullname, email))

        for _ in range(TASK_COUNT):
            title = fake.sentence(nb_words = 2)
            description = fake.sentence()
            status_id = randint(1, STATUS_COUNT)
            user_id = randint(1, USERS_COUNT)
            c.execute(sql_stmt_tasks, (title, description, status_id, user_id))
        
        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    try:
        with create_connect() as conn:
            insert_data(conn)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
    except DatabaseError as err:
        logging.error(f"Database error: {err}")



