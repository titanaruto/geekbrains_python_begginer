# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
import random
from functools import reduce

even_numbers = [x for x in [random.randint(100, 1000) for x in range(10)] if x % 2 == 0]

sum_numbers = reduce((lambda x, y: x + y), even_numbers)
print(even_numbers)
print(sum_numbers)
