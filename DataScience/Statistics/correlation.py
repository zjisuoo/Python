from collections import Counter
# from scratch.linear_algebra import sum_of_squares, dot
from typing import List
import matplotlib.pyplot as plt
import math

num_friends = [100, 90, 49, 41, 45, 39, 19, 17, 15, 13, 11, 33, 39, 51, 71, 91, 30, 7, 16, 81]
daily_minutes = [10, 20, 30, 40, 50, 60, 70, 15, 25, 45, 35, 24, 23, 13, 14, 15, 11, 9, 10, 11]
daily_hours = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8]

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
print('총 회원 수:', num_points, ' 최댓값:', largest_value, ' 최솟값:', smallest_value)

sorted_values = sorted(num_friends)
print(sorted_values)

# 중심 경향성
def mean(xs : List[float]) -> float :
    return sum(xs) / len(xs)

print('중심 경향성:', mean(num_friends))

# 분산 = 산포도를 측정
def de_mean(xs : List[float]) -> List[float] :
    x_bar = mean(xs) # x 의 모든 데이터 포인트에서 평균을 뺸다.
    return [ x - x_bar for x in xs]

def variance(xs : List[float]) -> float :
    assert len(xs) >= 2, "variance requires at least two elements" 
    # 편차 제곱의 평균 
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

# 표준 편차 = 분산의 제곱근
def standard_deviation(xs : List[float]) -> float :
    return math.sqrt(variance(xs))

def interquartile_range(xs : List[float]) -> float :
    return quantile(xs ,0.75) - quantile(xs, 0.25)

# 공분산
def covariance(xs : List[float], ys : List[float]) -> float :
    assert len(xs) == len(ys), "xs and ys must have same number of elements"

    return dot(de_mean(xs), de_mean(ys))/(len(xs) - 1)

# 상관관계
def correlation(xs : List[float], ys : List[float]) -> float :
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0 :
        return covariance(xs, ys) / stdev_x / stdev_y
    else :
        return 0
    
    print(correlation(num_friends, daily_minutes))
