# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

two_dimensional_matrix = [
    [1, 2],
    [30, 43],
    [31, 86]
]
three_dimensional_matrix = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]
]
four_dimensional_matrix = [
    [3, 5, 8, 3],
    [8, 3, 7, 1],
    [8, 3, 7, 1],
]


class Matrix:
    def __init__(self, list_args):
        self.list_args = list_args

    def __add__(self, other):
        result = Matrix(None)
        result.list_args = self.sum_matrix(self.list_args, other.list_args)
        return result

    def __str__(self):
        string = "\n".join(str(x) for x in self.list_args)
        return f"{string}\n"

    @staticmethod
    def sum_matrix(first_matrix, two_matrix):
        try:
            result = []
            for elm in first_matrix:
                index_first = first_matrix.index(elm)
                temp = []
                for value in elm:
                    index_two = elm.index(value)
                    sum_value = int(value) + int(two_matrix[index_first][index_two])
                    temp.append(sum_value)
                result.append(temp)
            return result
        except (IndexError, ValueError):
            return "Матрицы не соответствуют размеру друг друга"


if __name__ == "__main__":
    matrix_four_one = Matrix(four_dimensional_matrix)
    matrix_four_two = Matrix(four_dimensional_matrix)
    a = matrix_four_one + matrix_four_two
    print(a)
    matrix_three_one = Matrix(three_dimensional_matrix)
    matrix_three_two = Matrix(three_dimensional_matrix)
    b = matrix_three_one + matrix_three_two
    print(b)
    matrix_two_one = Matrix(two_dimensional_matrix)
    matrix_two_two = Matrix(two_dimensional_matrix)
    c = matrix_two_one + matrix_two_two
    print(c)
