import databases.config as config
import importlib
import os

print("Начало")

folder_modules = 'modules'
folder_modules_path = config.myRepo+'/' +folder_modules
modules_list = [os.path.splitext(file)[0] for file in os.listdir(folder_modules_path) if file.endswith('.py')]
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(f"{config.folder_name}.{folder_modules}.{module}")
    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']
ssh = imported_modules['ssh']
mysql = imported_modules['mysql']


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
ssh_client = ssh.create_ssh_tunnel(ssh_host, ssh_user, ssh_password, remote_bind_address, local_bind_port)

if ssh_client:
    # Подключение к базе данных через туннель
    db_connection = mysql.connect_to_database('127.0.0.1', 'u96142', os.environ['db_password'], 'u96142_sushi', 3306)

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

        fetch_all_from_table(db_connection, 'metro')

        db_connection.close()  # Закрываем соединение после выполнения запроса

    ssh_client.close()  # Закрываем SSH-туннель

print("Конец")