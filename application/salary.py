from datetime import datetime


def calculate_salary():
    now = datetime.now()
    print(f"Дата: {now.day}.{now.month}.{now.year}. Выполнилась функция \"calculate_salary\"")
