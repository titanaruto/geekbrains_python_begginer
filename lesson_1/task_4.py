# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while
# и арифметические операции.

# while True:
#     number = int(input("Введите целое положительное число: "))
#     if number > 0:
#         break

number = 31213123155534760123
max_number = 0
string_numbers = str(number)

for element in string_numbers:
    if max_number < int(element):
        max_number = int(element)

print(max_number)