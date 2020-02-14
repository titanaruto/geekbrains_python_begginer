# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    """

    :param args:
    :return:
    """
    values = list(args)
    first_value = max(values)
    values.remove(first_value)
    two_value = max(values)
    return first_value + two_value


print(my_func(10, 15, 23))
