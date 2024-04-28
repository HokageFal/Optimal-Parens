import random

def optimal_structure(p, n):

    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[i + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k


    return s


def print_matrix(p, n):
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    print("Матрица s")
    for i in range(1, len(s)):
        print(s[i][1:])

    print("Матрица m")
    for i in range(1, len(m)):
        print(m[i][1:])

    print(f"Минимальное количество скалярных умножений: {m[1][n]}")

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
def generate_matrices(p):
    matrices = []
    for i in range(len(p) - 1):
        rows = p[i]
        cols = p[i + 1]
        matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
        matrices.append(matrix)
    return matrices

def matrix_multiplication(first_matrix, second_matrix):


    if len(first_matrix[0]) != len(second_matrix):
        raise ValueError("Несовместимые размеры матриц для умножения.")

    result_matrix = [[0 for _ in range(len(second_matrix[0]))] for _ in range(len(first_matrix))]

    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

    return result_matrix



def multiply_matrices(matrices, s, i, j):

    if i == j:
        return matrices[i]
    else:
        left = multiply_matrices(matrices, s, i, s[i][j])
        right = multiply_matrices(matrices, s, s[i][j] + 1, j)
        return matrix_multiplication(left, right)


p = [10, 15, 20, 30, 20, 10, 15]
n = len(p) - 1

s = optimal_structure(p, n)

print_matrix(p, n)

print("Оптимальная расстановка скобок: ", end="")
print_optimal_parens(s, 1, n)

matrices = generate_matrices(p)

for idx, matrix in enumerate(matrices):
    print(f"\nMatrix {idx + 1} ({len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(row)
    print()

final_matrix = multiply_matrices(matrices, s, 1, n-1)

print("Итоговая матрица:")
for row in final_matrix:
    print(row)