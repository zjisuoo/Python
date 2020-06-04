from typing import List, NamedTuple
from collections import Counter
from linear_algebra import Vector, distance

def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

# assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'

def majority_vote(labels: List[str]) -> str:
    """Assumes that labels are ordered from nearest to farthest."""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

# Tie, so look at first 4, then 'b'
# assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'


from typing import NamedTuple
from linear_algebra import Vector, distance

class LabeledPoint(NamedTuple):
    point: Vector
    label: int

def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:

    # Order the labeled points from nearest to farthest.
    by_distance = sorted(labeled_points,
                         key=lambda air_index: distance(air_index.point, new_point))

    # Find the labels for the k closest
    k_nearest_labels = [air_index.label for air_index in by_distance[:k]]

    # and let them vote.
    return majority_vote(k_nearest_labels)

import random
import numpy as np

'''
def random_point(dim: int) -> Vector:
    return [random.random() for _ in range(dim)]

def random_distances(dim: int, num_pairs: int) -> List[float]:
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]
'''

def main():
    from typing import Dict
    import csv
    from collections import defaultdict
    
    def parse_air_row(row: List[str]) -> LabeledPoint:
        """
        cdate, fdust, ozone, nd, cm, sagas, airquality, air_index
        """
        measurements = [(value) for value in row[:-1]]
        # class is e.g. "Iris-virginica"; we just want "virginica"
        label = row[-1] #.split(",")[-1]
    
        return LabeledPoint(measurements, label)
    
    with open('./data2.csv') as f:
        reader = csv.reader(f)
        air_data = [parse_air_row(row) for row in reader]

    # 20180101,32,0.015,0.028,0.5,0.005,good,3
    # We'll also group just the points by species/label so we can plot them.
    points_by_species: Dict[str, List[Vector]] = defaultdict(list)
    for air in air_data :
        points_by_species[air.label].append(air.point)

    from matplotlib import pyplot as plt
    metrics = ['fdust', 'cm', 'sagas', 'air_index']
    pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
    marks = ['+', '.', 'x']  # we have 3 classes, so 3 markers
    
    fig, ax = plt.subplots(2, 3)
    
    for row in range(2):
        for col in range(2):
            i, j = pairs[3 * row + col]
            ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize = 8)
            ax[row][col].set_xticks([])
            ax[row][col].set_yticks([])
    
            for mark, (species, points) in zip(marks, points_by_species.items()):
                xs = [point[i] for point in points]
                ys = [point[j] for point in points]
                ax[row][col].scatter(xs, ys, marker=mark, label=species)
    
    ax[-1][-1].legend(loc='lower right', prop={'size': 6})
    plt.show()

    import random
    from machine_learning import split_data
    
    random.seed(12)
    air_train, air_test = split_data(air_data, 0.70)
    # assert len(air_train) == 0.7 * 150
    # assert len(air_test) == 0.3 * 150
    
    from typing import Tuple
    
    # track how many times we see (predicted, actual)
    confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)
    num_correct = 0
    
    for air in air_test:
        predicted = knn_classify(3, air_train, air.point)
        actual = air.label
    
        if predicted == actual:
            num_correct += 1
    
        confusion_matrix[(predicted, actual)] += 1
    
    pct_correct = num_correct / len(air_test)
    print(pct_correct, confusion_matrix)
    
    import tqdm
    dimensions = range(1, 101)
    
    avg_distances = []
    min_distances = []
    
    random.seed(0)
    for dim in tqdm.tqdm(dimensions, desc="Curse of Dimensionality"):
        distances = random_distances(dim, 10000)      # 10,000 random pairs
        avg_distances.append(sum(distances) / 10000)  # track the average
        min_distances.append(min(distances))          # track the minimum
    
    min_avg_ratio = [min_dist / avg_dist
                     for min_dist, avg_dist in zip(min_distances, avg_distances)]

    accuracy = np.mean(np.equal(air.label, air_test))
    right = np.sum(air.label * air_test == 1)
    precision = right / np.sum(air_test)
    recall = right / np.sum(air.label)
    f_score = 2 * precision * recall / (precision + recall)

    print('Accuracy : ', accuracy)
    print('Precision : ', precision)
    print('Recall : ', recall)
    print('F-score : ', f_score)

if __name__ == "__main__" : main()
