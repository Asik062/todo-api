import psycopg2

# Параметры подключения
host = "db"  # Имя сервиса в docker-compose
port = 5432
dbname = "todo_db"
user = "user"
password = "password"

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
        client_encoding='UTF8'
    )
    
    print("Подключение успешно!")

except Exception as e:
    print(f"Ошибка подключения: {e}")
finally:
    if connection:
        connection.close()
