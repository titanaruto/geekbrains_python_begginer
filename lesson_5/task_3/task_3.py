# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# first variant
# f_test = open("test.txt", "r")
# users_price = []
# for line in f_test:
#     users_price.append(line.split())
#
# middle_price = 0
# for last_name, price in users_price:
#     int_price = int(price)
#     if int_price < 20000:
#         print(last_name)
#     middle_price += int_price
#
# middle_price = middle_price / len(users_price)
# print(f"Средняя величина дохода сотрудников: {middle_price}")
# f_test.close()

# two variant
with open("test.txt", "r") as w_f_test:
    users_price = []
    for line in w_f_test:
        users_price.append(line.split())

    middle_price = 0

    for last_name, price in users_price:
        int_price = int(price)
        if int_price < 20000:
            print(last_name)
        middle_price += int_price

    middle_price = middle_price / len(users_price)
    print(f"Средняя величина дохода сотрудников: {middle_price}")