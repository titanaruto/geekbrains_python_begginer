# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# first variant
# f_test = open("test.txt", "r")
# lines = f_test.read().split("\n")
# print(f'Количество строк: {len(lines)}')
# for i, el in enumerate(lines):
#     print(f'Количество символов в {i + 1} строке: {len(el)}')
# f_test.close()

# two variant
with open("test.txt", "r") as w_f_test:
    lines = w_f_test.read().split("\n")
    print(f'Количество строк: {len(lines)}')
    for i, el in enumerate(lines):
        print(f'Количество символов в {i + 1} строке: {len(el)}')
