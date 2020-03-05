# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyClassException(Exception):
    def __init__(self, text):
        self.txt = text


def division_number(first_number, two_number):
    if two_number == 0:
        raise MyClassException("Нельзя делить на ноль")
    else:
        return first_number / two_number


if __name__ == '__main__':
    try:
        args = int(input("Введите число:"))
        print(division_number(10, args))
    except MyClassException as er:
        print(er)
