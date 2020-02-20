# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
numbers = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Ten": "Десять",
}
# first variant
# f_test = open("test.txt", "r")
# list_result = []
# for line in f_test:
#     elements = line.split()
#     for key, val in enumerate(elements):
#         try:
#             elements[key] = numbers[val]
#         except KeyError as e:
#             pass
#         except Exception as e:
#             print(e)
#     list_result.append(" ".join(elements))
# f_test.close()
# f_new = open("new.txt", "w")
# f_new.writelines("\n".join(list_result))

# two variant
with open("test.txt", "r") as w_f_test:
    list_result = []
    for line in w_f_test:
        elements = line.split()
        for key, val in enumerate(elements):
            try:
                elements[key] = numbers[val]
            except KeyError as e:
                pass
            except Exception as e:
                print(e)
        list_result.append(" ".join(elements))

with open("new.txt", "w") as w_f_new:
    w_f_new.writelines("\n".join(list_result))