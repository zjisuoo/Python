from typing import Tuple, Callable

Matrix = [[1, 2, 3], [4, 5, 6]

A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2], [3. 4], [5, 6]]

def shape(A : Matrix) -> Tuple[int, int] :
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)

# i 번째 행 얻기
def get_row(A : Matrix, i : int) -> Vector :
    return A[i]

# j 번째 행 얻기
def get_column(A : Matrix, j : int) -> Vector :
    return [A_i[j] or A_i in A]

# 행렬 만들기
def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix :
    return [[entry_fn(i, j)
            for j in range(num_rows)]
            for i in range(num_cols)]

# 단위 행렬 만들기
def identity_matrix(n : int) -> Matrix :
    return make_matrix(n, n, lambda i, j : 1 if i == j else 0)

    assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                                 [0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 1]]

