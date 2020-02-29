# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    __color = [("желтый", 2, 2), ("зеленый", 4, 3), ("красный", 7, 1)]
    __work = False

    def __init__(self):
        self.__work = True
        self.__running()

    def __get_work(self):
        return self.__work

    def __running(self):
        work_temp = self.__get_work()
        if work_temp:
            sort_colors = sorted(self.__color, key=lambda index: index[2])
            while work_temp:
                for element in sort_colors:
                    color, time_sleep, *other = element
                    print(f"Горит {color} цвет.")
                    time.sleep(int(time_sleep))


if __name__ == "__main__":
    start = TrafficLight()
