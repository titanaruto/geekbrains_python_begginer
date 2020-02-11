# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# item_list = list()
#
# while True:
#     element = input("Введите значение или завершите процесс введя слово 'стоп'")
#     if element == 'стоп':
#         break
#     else:
#         item_list.append(element)

item_list = ["test", 1231, True, 12.5, "Hello", 21, 17.5]
result_list = list()
if len(item_list) % 2 != 0:
    result_list_first = item_list[0:-1:2]
    result_list_two = item_list[1:-1:2]
    last_element = item_list[-1]
else:
    result_list_first = item_list[::2]
    result_list_two = item_list[1::2]
    last_element = None

for item in range(len(result_list_first)):
    result_list.append(result_list_two[item])
    result_list.append(result_list_first[item])

if last_element is not None:
    result_list.append(last_element)

print(item_list)
print(result_list)



