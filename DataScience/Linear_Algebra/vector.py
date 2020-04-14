from typing import List
import math

Vector = List[float]

height_weight_age = [70, 170, 40] # [inches, pounds, years]
grades = [95, 80, 75, 61] # [Exam 1, Exam 2, Exam 3, Exam 4]

# 벡터 합
def add(v : Vector, w : Vector) -> Vector :
    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6] == [5, 7, 9])

# 벡터 차
def subtract(v : Vector, w : Vector) -> Vector :
    assert len(v) == len(w)

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6] == [1, 2, 3]) 

# 벡터 성분의 합
def vector_sum(vectors : List[Vector]) -> Vector :
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different size!"

    return [sum(vectors[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2,], [3, 4], [5, 6], [7, 8]]) == [16, 20]

# 벡터와 스칼라 곱
def scalar_multiply(c : float, v : Vector) -> Vector :
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# 벡터의 성분별 평균
def vector_mean(vectors : List[Vector]) -> Vector :
    n = len(vectors)

    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# 벡터의 내적
def dot(v : Vector, w : Vector) -> float :
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i, in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

# 벡터 제곱의 합
def sum_of_squares(v : Vector) -> float :
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

# 벡터의 크기
def magnitude(v : Vector) -> float :
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5

# 벡터의 거리
def squared_distance(v : Vector, w : Vector) -> float :
    return sum_of_squares(subtract(v, w))

def distance(v : Vector, w : Vector) -> float :
    return math.sqrt(squared_distance(v, w))

def diastance(v : Vector, w : Vector) -> float :
    return magnitude(subtract(v, w))