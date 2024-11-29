import sqlite3

def create_connection(db_file):
    """Создает соединение с базой данных SQLite."""
    connection = sqlite3.connect(db_file)
    return connection

def show_tables(connection):
  """Функция для отображения всех таблиц в базе данных."""
  try:
      cursor = connection.cursor()
      cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

      tables = cursor.fetchall()
      print("Существующие таблицы:")
      for table in tables:
          print(table[0])  # Печатаем имя каждой таблицы

  except Exception as e:
      print(f"Ошибка при выполнении запроса: {e}")

  finally: cursor.close()

