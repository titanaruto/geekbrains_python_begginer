# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def determination_of_tissue_consumption(self):
        pass

    def __str__(self):
        return f"{self.name}"


class Coat(Clothes):
    def __init__(self, name, ):
        super().__init__(name)
        self._size = None

    size = property()

    @size.getter
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @size.deleter
    def size(self):
        self._size = ""

    def determination_of_tissue_consumption(self):
        try:
            return float(self._size / 6.5 + 0.5)
        except Exception as e:
            print(e)


class Costume(Clothes):
    def __init__(self, name, ):
        super().__init__(name)
        self._height = None

    height = property()

    @height.getter
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @height.deleter
    def height(self):
        self._height = ""

    def determination_of_tissue_consumption(self):
        try:
            return float(2 * self._height + 0.3)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    coat = Coat("пальто")
    coat.size = 42.3
    a = coat.determination_of_tissue_consumption()
    print(a)
    print(coat)
    costume = Costume("Костюм")
    costume.height = 42.3
    b = costume.determination_of_tissue_consumption()
    print(b)
    print(costume)
