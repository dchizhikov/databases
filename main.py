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
sql = imported_modules['sql']

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
        sql.show_tables(db_connection)
        sql.fetch_all_from_table(db_connection, 'metro')

        db_connection.close()

    ssh_client.close()
print("Конец")