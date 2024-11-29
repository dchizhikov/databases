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

sql = imported_modules['sql']
sqlite = imported_modules['sqlite']


# Устанавливаем соединение с базой данных
database = 'databases/sqlite/my_database.db'
connection = sqlite.create_connection(database)
sqlite.show_tables(connection)
# Определяем имя таблицы и столбцы
table_name = 'Users2'
columns = [
    'id INTEGER PRIMARY KEY',
    'username TEXT NOT NULL',
    'email TEXT NOT NULL',
    'age INTEGER'
]

# Создаем таблицу
sql.create_table(connection, table_name, columns)

# Добавляем пользователей
sql.add_user(connection, 'Alice2', 'alice@example.com', 302)
sql.add_user(connection, 'Bob2', 'bob@example.com', 252)
sql.add_user(connection, 'Charlie2', 'charlie@example.com', 352)

# Извлекаем и выводим всех пользователей
users = sql.fetch_users(connection)
for user in users:
    print(user)

# Закрываем соединение
connection.close()



print("Конец")