import sqlite3
import logging
from sqlite3 import Error

# Создание соединения с базой данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        logging.info("Connection to SQLite DB successful")
    except Error as e:
        logging.info(f"The error '{e}' occurred")
    return connection


# Проверка данных пользователя в базе данных
def login(username, password):
    db = create_connection("user.db")
    cursor = db.cursor()

    cursor.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
    db.commit()
    if not cursor.fetchone():
        logging.info("Нет такой записи")
        return
    else:
        logging.info('Welcome')
        return True
        # 'admin', '12345qwer'

# Добавление нового пользователя в базу данных
def reg(username, password):
    db = create_connection("user.db")
    cursor = db.cursor()
    try:
        cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        db.commit()
        logging.info("Ok")
        return True
    except Exception as e:
        logging.info('Error')
        return
