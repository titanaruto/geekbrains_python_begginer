# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result_list = []
with open("items.txt", "r") as f_items:
    items = f_items.read().split("\n")
    for el in items:
        name_item, numbers = el.split(":")

        number = 0
        numbers_clear = ""
        for symbol in numbers:
            # first variant
            # if symbol not in ["(", ")", ".", "п", "р", "л", "а", "б", "—"]:
            #     numbers_clear = "".join([numbers_clear, symbol])
            # two variant
            if symbol == " ":
                numbers_clear = "".join([numbers_clear, symbol])
            else:
                try:
                    symbol_int = int(symbol)
                    numbers_clear = "".join([numbers_clear, symbol])
                except (TypeError, ValueError) as e:
                    pass

        numbers = numbers_clear.split()
        sum_numbers = 0
        for number in numbers:
            sum_numbers += int(number)

        result_list.append([name_item, sum_numbers])

dict_items = dict(result_list)
print(dict_items)
