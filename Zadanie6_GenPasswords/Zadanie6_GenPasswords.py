import random
import string
import hashlib
import sqlite3
from datetime import datetime, timedelta

# Создание базы данных или подключение к существующей
conn = sqlite3.connect('paroli')
cursor = conn.cursor()

# Создание таблицы для хранения информации о пользователях
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password_hash TEXT,
        expiry_date TEXT
    )
''')
conn.commit()

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_user_password(username, password_length, password_expiry_days):
    # Генерация пароля
    password = generate_password(password_length)

    # Хэширование пароля
    hashed_password = hash_password(password)

    # Рассчитываем срок действия пароля
    expiry_date = (datetime.now() + timedelta(days=password_expiry_days)).strftime('%Y-%m-%d %H:%M:%S')

    # Добавление пользователя и пароля в базу данных
    cursor.execute('INSERT INTO users (username, password_hash, expiry_date) VALUES (?, ?, ?)',
                   (username, hashed_password, expiry_date))
    conn.commit()

    return password, expiry_date

if __name__ == "__main__":
    username = input("Введите имя пользователя: ")
    password_length = int(input("Введите длину пароля: "))
    password_expiry_days = int(input("Введите срок действия пароля (в днях): "))

    generated_password, expiry_date = generate_user_password(username, password_length, password_expiry_days)

    print(f"Сгенерированный пароль для пользователя {username}: {generated_password}")
    print(f"Срок действия пароля до {expiry_date}")

    # Закрываем соединение с базой данных
    conn.close()
