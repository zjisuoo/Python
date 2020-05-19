# 통계
from collections import Counter
# from scratch.linear_algebra import sum_of_squares, dot
import matplotlib.pyplot as plt
import math

num_friends = [100, 90, 49, 41, 45, 39, 19, 17, 15, 13, 11, 33, 39, 51, 71, 91, 30, 7, 16, 81]
daily_minutes = [10, 20, 30, 40, 50, 60, 70, 15, 25, 45, 35, 24, 23, 13, 14, 15, 11, 9, 10, 11]
daily_hours = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8, 2, 3, 4, 5, 6, 7]

friend_counts = Counter(num_friends)
xs = range(101) # 최댓값 100
ys = [friend_counts[x] for x in xs] # 히스토그램의 높이는 해당 친구 수를 갖고 있는 사용자의 수

plt.bar(xs, ys) 
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

# 중심 경향성
def mean(xs : List[float]) -> float :
    return sum(xs) / len(xs)

mean(num_friends)

# 중앙값 찾기
def _median_odd(xs : List[float]) -> float :
    return sorted(xs)[len(xs) // 2]

def _median_even(xs : List[float]) -> float :
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v : List[float]) -> float :
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

print(median(num_friends))

# 분위 = 중앙값을 포함하는 개념, 특정 백분위보다 낮은 분위에 속하는 데이터
def quantile(xs : List[float], p : float) -> float :
    p_index = int(p * len(s))
    return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13

# 최빈값 = 데이터에서 가장 자주 나오는 값
def mode(x : List[float]) -> List[float] :
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

assert set(mode(num_friends)) == {1, 6}

# 산포도 = 데이터가 얼마나 퍼져 있는지 나타냄
def data_range(xs : List[float]) -> float :
    return max(xs) -min(xs)

assert data_range(num_friends) == 99

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

assert 81.54 < variance(num_friends) < 81.55

# 표준 편차 = 분산의 제곱근
def standard_deviation(xs : List[float]) -> float :
    return math.sqrt(variance(xs))

assert 9.02 < standard_deviation(num_friends) < 9.04

def interquartile_range(xs : List[float]) -> float :
    return quantile(xs ,0.75) - quantile(xs, 0.25)

assert interquartile_range(num_friends) == 6

# 공분산
def covariance(xs : List[float], ys : List[float]) -> float :
    assert len(xs) == len(ys), "xs and ys must have same number of elements"

    return dot(de_mean(xs), de_mean(ys))/(len(xs) - 1)

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60

# 상관관계
def correlation(xs : List[float], ys : List[float]) -> float :
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0 :
        return covariance(xs, ys) / stdev_x / stdev_y
    else :
        return 0

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25


outlier = num_friends.index(100)

num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]
daily_minutes_good = [x for i, x in enumerate(daily_minutes) if i != outlier]
daily_hours_good = [dm / 60 for dm in daily_minutes_good]


assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58