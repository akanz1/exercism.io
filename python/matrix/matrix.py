class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
            list(map(lambda n: int(n), row.split()))
            for row in matrix_string.split("\n")
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return list(list(zip(*self.matrix))[index - 1])
