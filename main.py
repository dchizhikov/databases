import git.config as config
import importlib
import os

print("Начало")

folder_modules = 'modules'
folder_modules_path = 'git'+'/' +folder_modules #config.myRepo+'/' +folder_modules
modules_list = [os.path.splitext(file)[0] for file in os.listdir(folder_modules_path) if file.endswith('.py')]
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(f"{config.folder_name}.{folder_modules}.{module}")
    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']

#os.system('pip install mysql-connector-python')
#os.system('pip install paramiko mysql-connector-python')


import paramiko
import mysql.connector
from mysql.connector import Error

def create_ssh_tunnel(ssh_host, ssh_user, ssh_password, remote_bind_address, local_bind_port):
    """Создание SSH-туннеля."""
    try:
        # Создаем SSH-клиент
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Подключаемся к SSH-серверу
        ssh_client.connect(ssh_host, username=ssh_user, password=ssh_password, port=22)

        # Создаем туннель (локальный хост, локальный порт, удаленный хост, удаленный порт)
        transport = ssh_client.get_transport()
      # Создаем туннель (локальный хост, локальный порт, удаленный адрес)
        transport.request_port_forward('localhost:0', local_bind_port, remote_bind_address[0] + ':' + str(remote_bind_address[1]))

        print(f"SSH туннель установлен на порт {local_bind_port}")
        return ssh_client

    except Exception as e:
        print(f"Ошибка при создании SSH-туннеля: {e}")
        return None

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

# Параметры подключения
ssh_host = 'u96142.ssh.masterhost.ru'  # SSH сервер
ssh_user = 'u96142'                     # Логин SSH
ssh_password = os.environ['ssh_password']
remote_bind_address = ('u96142.mysql.masterhost.ru', 3306)  # Адрес вашего MySQL сервера
local_bind_port = 3306                   # Локальный порт для туннеля

# Создание SSH-туннеля
ssh_client = create_ssh_tunnel(ssh_host, ssh_user, ssh_password, remote_bind_address, local_bind_port)

if ssh_client:
    # Подключение к базе данных через туннель
  # Подключение к базе данных через туннель (используем локальный адрес и порт 3307)
    db_connection = connect_to_database('127.0.0.1', 'u96142', os.environ['db_password'], 'u96142_sushi', 3306)  # Указываем порт 3307

    if db_connection is not None:
        show_tables(db_connection)
        # Выполнение запроса SELECT * FROM metro
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

        fetch_all_from_table(db_connection, 'metro')  # Замените 'metro' на нужное имя таблицы

        db_connection.close()  # Закрываем соединение после выполнения запроса

    ssh_client.close()  # Закрываем SSH-туннель

print("Конец")