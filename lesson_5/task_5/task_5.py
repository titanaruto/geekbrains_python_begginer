# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("create.txt", "w") as f_create:
    list_of_numbers = input("Введите набор чисел: ")
    f_create.writelines(list_of_numbers)

with open("create.txt", "r") as f_read:
    list_of_numbers = f_read.read().split()
    sum_numbers = 0
    for el in list_of_numbers:
        sum_numbers += int(el)

    print(f"Сумма числе: {sum_numbers}")
