# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = {
    "зима": winter,
    "весна": spring,
    "лето": summer,
    "осень": autumn,
}

month = 0
while True:
    month = int(input("Введите номер месяц от 1 до 12: "))
    if month >= 1 and month <= 12:
        break

# .............. list
if month in winter:
    print("зима")
elif month in summer:
    print("лето")
elif month in autumn:
    print("осень")
elif month in spring:
    print("весна")
# ....................... dict
for key, val in seasons.items():
    if month in val:
        print(key)
