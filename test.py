import psycopg2

# Параметры подключения
host = "localhost"  # Или "db", если база в Docker
port = 5432
dbname = "todo_db"
user = "postgres"
password = "postgres"

# Создание строки подключения
connection_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

# Проверка строки подключения
print(f"Строка подключения: {connection_url}")

connection = None
try:
    # Попытка подключения к базе данных
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        client_encoding='UTF8'  # Устанавливаем кодировку
    )
    
    print("Подключение успешно!")

except Exception as e:
    print(f"Ошибка подключения: {e}")
finally:
    if connection:
        connection.close()
