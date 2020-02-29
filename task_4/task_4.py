# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина  {self.name} Остановилась")

    def turn(self, direction):
        print(f"Поворот на {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        if self.speed > self.__max_speed:
            print(f"Вы привысели максимальную ({self.__max_speed}) скорость , ваша скорость: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        if self.speed > self.__max_speed:
            print(f"Вы привысели максмильную ({self.__max_speed}) скорость , ваша скорость: {self.speed}")


class PoliceCar(Car):
    is_police = True


# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
if __name__ == "__main__":
    town_car = TownCar(62, "зеленый", "Audi")
    work_car = WorkCar(43, "Синий", "Audi")
    sport_car = SportCar(120, "красный", "Ferrari")
    police_car = PoliceCar(60, "черный", "Police")
    town_car.go()
    town_car.turn("left")
    town_car.show_speed()
    town_car.stop()
    print()
    work_car.go()
    work_car.turn("left")
    work_car.show_speed()
    work_car.stop()
    print()
    sport_car.go()
    sport_car.turn("left")
    sport_car.show_speed()
    sport_car.stop()
    print()
    police_car.go()
    police_car.turn("left")
    police_car.show_speed()
    police_car.stop()
