# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# number = int(input("Введите число: "))
number = 3
sum_numbers = number + (number * 10 + number) + ((number * 10 + number) * 10 + number)

print(sum_numbers)
