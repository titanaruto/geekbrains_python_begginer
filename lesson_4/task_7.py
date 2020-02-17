# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def factorial_gen(number):
    temp = 1
    for i in range(temp, number + temp):
        temp = temp * i
        yield temp


n = 17
result = [el for el in factorial_gen(n)]

max_print = 15
print(result[:max_print])
for i, el in enumerate(result):
    if i == max_print:
        break
    else:
        print(el)
