# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_values = ["test", 1231, True, ["0", "text"], {0: "hello"}, (12, 25), None, 12.5, set("Hello")]

for item in list_values:
    if type(item) is None:
        print('NoneType')
    if type(item) == str:
        print('str')
    if type(item) == int:
        print('int')
    if type(item) == bool:
        print('bool')
    if type(item) == list:
        print('list')
    if type(item) == dict:
        print('dict')
    if type(item) == tuple:
        print('tuple')
    if type(item) == float:
        print('float')
    if type(item) == set:
        print('set')
