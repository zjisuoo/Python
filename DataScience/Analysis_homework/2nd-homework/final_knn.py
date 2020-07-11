from collections import Counter
from scratch.linear_algebra import distance, Vector
import math, random
import pandas as pd
from typing import TypeVar, List, Tuple, Dict, NamedTuple
from collections import defaultdict
X = TypeVar('X')  # generic type to represent a data point

"""raw_majority_vote에서 공동일등이 생길때 단독 1등이 생길 때까지 k를 하나씩 줄이기 위한 함수"""
def majority_vote(labels): # label은 k개의 가까운 이웃을 받은 것이다.
    """labels는 가장 가까운 데이터부터 가장 먼 데이터 순서로 정렬되어 있다고 가정"""
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner  # unique winner, so return it, 1등이 하나이다.
    else:
        return majority_vote(labels[:-1])  # try again without the farthest, 가장 먼 데이터를 제외하고 다시 찾는다.

class LabeledPoint(NamedTuple):
    point: Vector
    label: str

def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest, 
    # 레이블된 포인트를 가장 가까운 데이터부터 가장 먼 데이터 순서로 정렬
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))

    # find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)

#  공기질/ 레이블로 무리 짓는다.
def parse_air_data(row: List[str]) -> LabeledPoint:
    measurements = [float(value) for value in row[:-1]]
    label = row[-1]
    return LabeledPoint(measurements, label)

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:]                    # Make a shallow copy
    # random.shuffle(data)              # because shuffle modifies the list.
    cut = int(len(data) * prob)       # Use prob to find a cutoff
    return data[:cut], data[cut:]     # and split the shuffled list there.

def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    try:
        return tp / (tp + fp)
    except ZeroDivisionError:
        return 0.0

def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fn)

def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    try:
        p = precision(tp, fp, fn, tn)
        r = recall(tp, fp, fn, tn)

        return 2 * p * r / (p + r)
    except ZeroDivisionError:
        return 0.0

if __name__ == "__main__":
    # data2.csv를 읽어오기 위해서 pandas를 사용했습니다.
    dataFrame = pd.read_csv('datascience/microdust_analysis_by_KNN/data2.csv', encoding='CP949')
    inputs = dataFrame[['fdust', 'ozone', 'nd', 'cm', 'sagas', 'airquality']].values.tolist()
    
    air_data = [parse_air_data(row) for row in inputs]
    
    points_by_airquality: Dict[str, List[Vector]] = defaultdict(list)
    for air in air_data:
        points_by_airquality[air.label].append(air.point)
    
    # train_data와 test_data를 나눔
    air_train, air_test = split_data(air_data, 0.7)

    # (predicted, actual)을 몇 번 살펴보는지 추적
    confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)
    num_correct = 0

    # data별로 K-NN 실행(n=3)
    for air in air_data:
        predicted = knn_classify(2, air_train, air.point)
        actual = air.label

        if predicted == actual:
            num_correct += 1

        confusion_matrix[(predicted, actual)] += 1

    name_list = ['best', 'better', 'good', 'normal', 'bad', 'worse', 'serious', 'worst']
    check_dict = {}

    TOTAL_TEST = sum([confusion_matrix[key] for key in confusion_matrix.keys()]) # 7538

    for idx, name in enumerate(name_list):
        tp, fp, fn, tn = 0, 0, 0, 0
        for i in range(len(name_list)):        
            try:
                if(idx == i): # 현재 확인하는 label이 동일하다.
                    tp = confusion_matrix[name, name]
                else:
                    fp = confusion_matrix[name, name_list[i]] + fp
                    fn = confusion_matrix[name_list[i], name] + fn 
            except KeyError:
                pass

        check_dict[name] = [tp, fp, fn, (TOTAL_TEST-(tp+fp+fn))]

    for i in range(8):
        print(name_list[i]+' precision', 
                precision(check_dict[name_list[i]][0], check_dict[name_list[i]][1], check_dict[name_list[i]][2], check_dict[name_list[i]][3]))

        print(name_list[i]+' recall', 
                recall(check_dict[name_list[i]][0], check_dict[name_list[i]][1], check_dict[name_list[i]][2], check_dict[name_list[i]][3]))

        print(name_list[i]+' f1_score', 
                f1_score(check_dict[name_list[i]][0], check_dict[name_list[i]][1], check_dict[name_list[i]][2], check_dict[name_list[i]][3]))
        print()