#import mysql.connector
from mysql.connector import Error

def fetch_all_from_table(connection, table_name):
    """Функция для получения всех записей из указанной таблицы."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")

        # Получаем все строки результата
        rows = cursor.fetchall()

        print(f"Записи из таблицы {table_name}:")
        for row in rows:
            print(row)

    except Error as e:
        print(f"Ошибка при выполнении запроса: {e}")

    finally:
        cursor.close()

def create_table(connection, table_name, columns):
    """Создает таблицу с заданным именем и столбцами."""
    cursor = connection.cursor()

    # Формируем SQL-запрос для создания таблицы
    columns_with_types = ', '.join(columns)
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})"

    cursor.execute(create_table_sql)
    connection.commit()

def add_user(connection, username, email, age):
    """Добавляет нового пользователя в таблицу Users."""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (username, email, age))
    connection.commit()

def fetch_users(connection):
    """Извлекает всех пользователей из таблицы Users."""
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    return cursor.fetchall()


