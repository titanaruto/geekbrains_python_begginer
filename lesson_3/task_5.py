# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

sum_numbers = 0
exit = False
while True:
    string_numbers = input("Введите строку чисел разделленые пробелом (введите 'EXIT' если хотите закрыть программу): ")
    if "EXIT" in string_numbers:
        string_numbers = string_numbers.split("EXIT")[0]
        exit = True

    list_string_numbers = string_numbers.split()
    list_numbers = []
    for element in list_string_numbers:
        list_numbers.append(int(element))
    sum_numbers += sum(list_numbers)
    if exit:
        break
    print(f"Сумма чисел: {sum_numbers}")

print(f"Сумма всех чисел: {sum_numbers}")
