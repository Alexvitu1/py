'''
Задание 3. Планирование задач

Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
'''
from datetime import datetime, timedelta


def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество
    дней от текущей даты.
    :param days_from_now: Количество дней от текущей даты.
    :return: Отформатированная дата в формате YYYY-MM-DD.
    Примеры:
    >>> future_date(30)
    '2024-11-13'
    >>> future_date(-10)
    '2024-10-04'
    """
    # Получение текущей даты и времени
    today = datetime.now()

    # Вычисление даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)

    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    days = 30  # Количество дней для вычисления
    print(f'Date {days} days from now: {future_date(days)}')