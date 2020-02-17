# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
import random

randoms_number = [x for x in [random.randint(20, 240) for x in range(1000)] if x == 20 or x == 21]
print(randoms_number)
