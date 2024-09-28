import psycopg2
from config_db import *

def make_connection():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=dbname,
        port=port
    )

def select_users():
    # Создание подключения
    c = make_connection()
    cursor = c.cursor()
    # Выполнение запроса
    cursor.execute("SELECT * FROM users;")
    # Получение всех результатов
    users = cursor.fetchall()
    # Закрываем соединение
    c.close()
    # Возвращаем все строки результата
    return users

def add_user_minerva():
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("INSERT INTO users (entity_type, login, password, admin, enabled, surname, firstname, email, "
                   "email_accepted, registration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, now())",
                   (entity_type_kms, user_kms, password_kms, admin_kms, enabled_kms, surname_kms, firstname_kms,
                    email_kms, email_accepted_kms))
    c.commit()
    c.close()

add_user_minerva()

def select_from_test():
    c = make_connection()
    cursor = c.cursor()
    cursor.execute("SELECT * FROM test")
    tests = cursor.fetchall()
    c.close()
    return tests

# tests = select_from_test()
# for test in tests:
#     print(test)

# Печать всех пользователей
users = select_users()
for user in users:
    print(user)