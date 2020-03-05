# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class MyDateError(Exception):
    def __init__(self, text):
        self.txt = text


class MyData:
    def __init__(self, date_string):
        self._date_string = date_string

    @staticmethod
    def is_corrected_number(day, month, year):
        if type(day) == int and type(month) == int and type(year) == int:
            if day <= 0 or day > 32:
                raise MyDateError("Не бывает такое количество дней")
            if month <= 0 or month > 12:
                raise MyDateError("Не существует такого месяца")
            if year <= 0:
                raise MyDateError("Не существует такого года")
        else:
            raise MyDateError("Введите дату формата 00-00-0000")
        return True

    @classmethod
    def is_corrected_date(cls, date_string):
        try:
            day, month, year = map(int, str(date_string).split("-"))
            return cls.is_corrected_number(day, month, year)
        except ValueError as e:
            raise MyDateError("Введите дату формата 00-00-0000")



if __name__ == '__main__':
    my_date = MyData("12-02-2020")
    try:
        print(my_date.is_corrected_date("02-10-2012"))
    except MyDateError as err:
        print(err)
