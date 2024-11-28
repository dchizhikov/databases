#import mysql.connector
from mysql.connector import Error

def show_tables(connection):
  """Функция для отображения всех таблиц в базе данных."""
  try:
      cursor = connection.cursor()
      cursor.execute("SHOW TABLES;")

      tables = cursor.fetchall()
      print("Существующие таблицы:")
      for table in tables:
          print(table[0])  # Печатаем имя каждой таблицы

  except Error as e:
      print(f"Ошибка при выполнении запроса: {e}")

  finally: cursor.close()

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