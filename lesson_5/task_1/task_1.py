# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
list_text = []
while True:
    text = input("Введите текст: ")
    if len(text) == 0:
        break
    else:
        list_text.append(f'{text}\n')

# first variant
# my_f = open("task_1/text.txt", "w")
# my_f.writelines(list_text)
# my_f.close()

# two variant
with open("task_1/text.txt", "w") as w_my_f:
    w_my_f.writelines(list_text)
