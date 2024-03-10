import logging
from psycopg2 import DatabaseError

from connect import create_connect

def request(conn, sql_stmt):
    c = conn.cursor()
    try:
        c.execute(sql_stmt)
        result = c.fetchall()
       # conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()
    return result

# 1. Отримати всі завдання певного користувача. (user_id = 15)
sql_stmt_1 = """SELECT title, description FROM tasks WHERE user_id = 15;"""

# 2. Вибрати завдання за певним статусом. (status - 'new')
sql_stmt_2 = """SELECT title FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = 'new');"""

# 3. Оновити статус конкретного завдання. 
sql_stmt_3 = """UPDATE tasks SET status_id = 2 WHERE id =5;"""

# 4. Отримати список користувачів, які не мають жодного завдання. 
sql_stmt_4 = """SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);"""

# 5. Додати нове завдання для конкретного користувача. 
sql_stmt_5 = """INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('task1', 'new task 1', 1, 1);"""

# 6. Отримати всі завдання, які ще не завершено. 
sql_stmt_6 = """SELECT * FROM tasks WHERE status_id NOT IN (SELECT id FROM status WHERE name = 'completed');"""

# 7. Видалити конкретне завдання. (with id = 7)
sql_stmt_7 = """DELETE FROM tasks WHERE id = 7;"""

# 8. Знайти користувачів з певною електронною поштою. 
sql_stmt_8 = """SELECT * FROM users WHERE email LIKE '%.com';"""

# 9. Оновити ім'я користувача. (for user with id = 15)
sql_stmt_9 = """UPDATE users SET fullname = 'Maksim' WHERE id = 15;"""

# 10. Отримати кількість завдань для кожного статусу.
sql_stmt_10 = """SELECT COUNT(id) AS tasks_count, status_id
FROM tasks
GROUP BY status_id;"""

# 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
sql_stmt_11 = """SELECT u.fullname, t.title, u.email
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id
WHERE u.email LIKE '%@example.org';"""

# 12. Отримати список завдань, що не мають опису.
sql_stmt_12 = """SELECT id, title FROM tasks WHERE description = '';"""

# 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
sql_stmt_13 = """SELECT u.fullname, t.title AS task_title, t.status_id 
FROM tasks AS t 
INNER JOIN users AS u ON u.id = t.user_id
WHERE t.status_id = 2;"""

# 14. Отримати користувачів та кількість їхніх завдань.  
sql_stmt_14 = """SELECT u.fullname, COUNT(t.id) AS tasks_count, t.user_id 
FROM tasks AS t
LEFT JOIN users AS u ON u.id = t.user_id
GROUP BY t.user_id, u.fullname;"""

if __name__ == "__main__":
    try:
        with create_connect() as conn:
            print(request(conn, sql_stmt_2))
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
    except DatabaseError as err:
        logging.error(f"Database error: {err}")