from datetime import datetime


def get_employees():
    now = datetime.now()
    print(f"Дата: {now.day}.{now.month}.{now.year}. Выполнилась функция \"get_employees\"")
