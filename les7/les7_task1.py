
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        tmp_matrix = []
        tmp_vector = []
        for n in range(len(self.my_list)):
            tmp_vector.clear()
            for m in range(len(self.my_list[n])):
                tmp_vector.append(self.my_list[n][m] + other.item(n, m))
            tmp_matrix.append(tmp_vector)
        return Matrix(tmp_matrix)

    def item(self, n, m):
        return self.my_list[n][m]

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))


a = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])
b = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])

print(a + b)
