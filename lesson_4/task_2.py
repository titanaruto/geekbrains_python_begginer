# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
import random

set_of_numbers = []
result_numbers = []

for _ in range(10):
    set_of_numbers.append(random.randint(-100, 100))

for i in range(1, len(set_of_numbers)):
    if set_of_numbers[i] > set_of_numbers[i - 1]:
        result_numbers.append(set_of_numbers[i])

print(set_of_numbers)
print(result_numbers)
