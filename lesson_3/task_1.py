# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def get_division_number(number_1, number_2):
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
a = 0
b = 0
print(get_division_number(a, b))
