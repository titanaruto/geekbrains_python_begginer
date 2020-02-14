# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# first_variant realization
def my_func_1(x, y):
    if x > 0 and type(y) == int:
        return f"{x ** y:.2f}"
    else:
        print("Не коректно заданы числа")


# two_variant realization
def my_func_2(x, y):
    if  x > 0 and type(y) == int:
        result = x
        for iteration in range(1, abs(y)):
            result *= x
        if y < 0:
            result = 1 / result
        return f"{result:.2f}"
    else:
        print("Не коректно заданы числа")


number = 5.2
power = 2

print(my_func_1(number, power))
print(my_func_2(number, power))
