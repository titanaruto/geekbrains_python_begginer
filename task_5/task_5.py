# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class MyComplexNumber:

    def __init__(self, number):
        self._number = number

    def __add__(self, other):
        # sum_number = self._number
        # return MyComplexNumber(sum_number)
        pass

    def __mul__(self, other):
        pass


if __name__ == '__main__':
    number1 = MyComplexNumber("1+3i")
    number2 = MyComplexNumber("4-5i")
