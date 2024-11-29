#os.system('pip install mysql-connector-python')
import mysql.connector
from mysql.connector import Error

def connect_to_database(host, user, password, database, port):
  """Функция для подключения к базе данных MySQL с параметрами."""
  try:
      connection = mysql.connector.connect(
          host=host,
          user=user,
          password=password,
          database=database,
          port=port  # Указываем порт для подключения
      )

      if connection.is_connected():
          print("Успешно подключено к базе данных")
          return connection

  except Error as e:
      print(f"Ошибка при подключении к базе данных: {e}")
      return None

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