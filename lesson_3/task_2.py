# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


# first_variant realization
def print_user_information(**kwargs):
    values = {}
    for key, value in kwargs.items():
        values[key] = value
    print(
        f"Имя: {values['name']}, Фамилия: {values['last_name']}, дата рождения: {values['birthday']}, "
        f"Город проживания: {values['city']}, емейл: {values['email']}, телефон: {values['phone']}")


# two_variant realization
def print_user_information_2(name, last_name, birthday, city, email, phone):
    print(
        f"Имя: {name}, Фамилия: {last_name}, дата рождения: {birthday}, "
        f"Город проживания: {city}, емейл: {email}, телефон: {phone}")


print_user_information(last_name="Пузякин", name="Вася", birthday="23.02.1905", city="Москва", email="test@ts.as",
                       phone="21111111111")
