# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass_calculation_of_asphalt(self, mass_asphalt,
                                        thickness):
        sum_args = int((self.__get_area() * mass_asphalt * thickness) / 1000)
        return f"{sum_args} т"

    def __get_area(self):
        return self._length * self._width


if __name__ == "__main__":
    road = Road(30, 5000)
    mass = road.get_mass_calculation_of_asphalt(25, 5)
    print(mass)
