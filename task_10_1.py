class Matrix:
    def __init__(self, matrix_list: list):
        for i in range(1, len(matrix_list)):
            if len(matrix_list[i-1]) == len(matrix_list[i]):
                pass
            else:
                raise TypeError('lines in matrix should be only same length')
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for matrix_str in self.matrix_list:
            result += f'{matrix_str}\n'
        return f'\n{result}'  # пустую строку до и после матрицы оставил специально, чтобы отделить матрицу от остальных выводов

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list):
            if len(self.matrix_list[0]) == len(other.matrix_list[0]):
                result_matrix = []
                for i in range(len(self.matrix_list)):
                    result_matrix.append(list(map(sum, zip(self.matrix_list[i], other.matrix_list[i]))))
                return Matrix(result_matrix)
        raise TypeError('You can only add matrices of the same size')


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(a)

print(b)

c = a + b

print(c)


