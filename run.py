import time
from sqlalchemy.exc import OperationalError
from app import create_app, db

app = create_app()

# Попытка подключения к базе данных с повтором
with app.app_context():
    connected = False
    for i in range(10):
        try:
            db.create_all()
            connected = True
            break
        except OperationalError:
            print("База ещё не готова, пробуем снова...")
            time.sleep(2)
    if not connected:
        print("Не удалось подключиться к БД.")
        exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
