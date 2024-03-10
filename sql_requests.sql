-- Отримати всі завдання певного користувача. (user_id = 15)
SELECT title, description FROM tasks WHERE user_id = 15;

-- Вибрати завдання за певним статусом.(status - 'new')
SELECT title FROM tasks WHERE status_id in (SELECT id FROM status WHERE name = 'new');

-- Оновити статус конкретного завдання. 
UPDATE tasks SET status_id = 2 WHERE id =5;

-- Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- Додати нове завдання для конкретного користувача. 
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('task1', 'new task 1', 1, 1);

-- Отримати всі завдання, які ще не завершено. 
SELECT * FROM tasks WHERE status_id NOT IN (SELECT id FROM status WHERE name = 'completed');

-- Видалити конкретне завдання. (with id = 7)
DELETE FROM tasks WHERE id = 7;

-- Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE '%.com';

-- Оновити ім'я користувача. (for user with id = 15)
UPDATE users SET fullname = 'Maksim' WHERE id = 15;

-- Отримати кількість завдань для кожного статусу.
SELECT COUNT(id) as tasks_count, status_id
FROM tasks
GROUP BY status_id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT u.fullname, t.title, u.email
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id
WHERE u.email LIKE '%@example.org';

UPDATE tasks SET description = '' WHERE id = 20;
-- Отримати список завдань, що не мають опису.
SELECT id, title FROM tasks WHERE description = '';

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT u.fullname, t.title AS task_title, t.status_id 
FROM tasks AS t 
INNER JOIN users AS u ON u.id = t.user_id
WHERE t.status_id = 2;

-- Отримати користувачів та кількість їхніх завдань.
SELECT u.fullname, COUNT(t.id) AS tasks_count, t.user_id 
FROM tasks AS t
LEFT JOIN users AS u ON u.id = t.user_id
GROUP BY t.user_id, u.fullname;






