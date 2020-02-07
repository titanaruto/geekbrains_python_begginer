# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте
# форматирование строк.

# seconds = int(input("Введите время в секундах: "))
seconds = 50000
minutes = int(seconds / 60)
hours = int(seconds / 3600)
minutes = minutes - (hours * 60)
list_seconds = list(str(seconds))
last_index = len(list_seconds) - 1
pre_last_index = len(list_seconds) - 2

seconds = f"{list_seconds[pre_last_index]}{list_seconds[last_index]}"
if int(seconds) > 60:
    seconds = int(seconds) - 60

if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'

print(f"время {hours}:{minutes}:{seconds}")
