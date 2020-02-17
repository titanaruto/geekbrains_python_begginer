# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
from itertools import count, cycle

start = 1
end = 10
values_other = ["Hello", "test", "Hi", "test2", "ssdasd"]
for el in count(start):
    if el > end:
        break
    else:
        print(el)
print()
conter_index = 0
for el in cycle(values_other):
    if conter_index > end:
        break
    print(el)
    conter_index += 1
