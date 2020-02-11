# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# words = input("Введите несколько слов через пробел")
words = "еуывыфвф выфыф вы 12345678901"

words_list = words.split()

result = list()
for item in words_list:
    if len(item) > 10:
        result.append(item[:10])
    else:
        result.append(item)

for ind, el in enumerate(result):
    print(ind, el)
