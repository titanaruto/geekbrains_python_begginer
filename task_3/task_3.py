# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
income_dict = {"wage": 100000, "bonus": 3000, "additional_wage": 2000}


class Worker:
    name = None
    surname = None
    position = None
    _income = income_dict

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        elements_temp = self._income.values()
        result = sum(map(lambda x: int(x), elements_temp))
        return result


if __name__ == "__main__":
    position_cls = Position("Петров", "Шредар", "Таксист")
    full_name = position_cls.get_full_name()
    price = position_cls.get_total_income()
    print(full_name)
    print(price)
