# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def get_division_number(number_1, number_2):
    """
    :param number_1:
    :param number_2:
    :return:
    """
    if number_2:
        try:
            number = number_1 / number_2
        except ZeroDivisionError:
            return "Ошибка: деление на ноль"
        else:
            return number
    else:
        print("Деление на ноль запрещено")


# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
a = 5
b = 15
print(get_division_number(a, b))
