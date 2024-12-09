'''
Задание 4. Опции и флаги

Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:

● --verbose, если этот флаг установлен, скрипт должен выводить
дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать,
сколько раз повторить строку в выводе.
'''
import argparse


def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями')
    # Добавление обязательных аргументов
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')

    # Добавление опций
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Вывод дополнительной информации')
    parser.add_argument('--repeat',
                        type=int,
                        default=1,
                        help='Количество повторений строки')
    # Парсинг аргументов
    args = parser.parse_args()

    # Вывод дополнительной информации, если опция verbose установлена
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, '
              f'text = "{args.text}", repeat = {args.repeat}')
    # Вывод строки, повторенной указанное количество раз
    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')

if __name__ == '__main__':
    main()