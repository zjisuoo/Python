from collections import Counter
from linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 문제 2에서 만든 data2.csv 사용
data = pd.read_csv("./data2.csv", encoding="utf-8")

airq = list()

for i in range(len(data)) :
    if data['air_index'][i] == 1 or data['air_index'][i] == 2 :
        val = (data['air_index'][i], data['fdust'][i], 'GOOD_AIR')
    elif data['air_index'][i] == 3 or data['air_index'][i] == 4 or data['air_index'][i] == 5 :
        val = (data['air_index'][i], data['fdust'][i], 'NORMAL_AIR')
    elif data['air_index'][i] == 6 or data['air_index'][i] == 7 or data['air_index'][i] == 8 :
        val = (data['air_index'][i], data['fdust'][i], 'BAD_AIR')
    airq.append(val)

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points, key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)

# cities = [(-86.75,33.5666666666667,'Python'),(-88.25,30.6833333333333,'Python'),(-112.016666666667,33.4333333333333,'Java'),(-110.933333333333,32.1166666666667,'Java'),(-92.2333333333333,34.7333333333333,'R'),(-121.95,37.7,'R'),(-118.15,33.8166666666667,'Python'),(-118.233333333333,34.05,'Java'),(-122.316666666667,37.8166666666667,'R'),(-117.6,34.05,'Python'),(-116.533333333333,33.8166666666667,'Python'),(-121.5,38.5166666666667,'R'),(-117.166666666667,32.7333333333333,'R'),(-122.383333333333,37.6166666666667,'R'),(-121.933333333333,37.3666666666667,'R'),(-122.016666666667,36.9833333333333,'Python'),(-104.716666666667,38.8166666666667,'Python'),(-104.866666666667,39.75,'Python'),(-72.65,41.7333333333333,'R'),(-75.6,39.6666666666667,'Python'),(-77.0333333333333,38.85,'Python'),(-80.2666666666667,25.8,'Java'),(-81.3833333333333,28.55,'Java'),(-82.5333333333333,27.9666666666667,'Java'),(-84.4333333333333,33.65,'Python'),(-116.216666666667,43.5666666666667,'Python'),(-87.75,41.7833333333333,'Java'),(-86.2833333333333,39.7333333333333,'Java'),(-93.65,41.5333333333333,'Java'),(-97.4166666666667,37.65,'Java'),(-85.7333333333333,38.1833333333333,'Python'),(-90.25,29.9833333333333,'Java'),(-70.3166666666667,43.65,'R'),(-76.6666666666667,39.1833333333333,'R'),(-71.0333333333333,42.3666666666667,'R'),(-72.5333333333333,42.2,'R'),(-83.0166666666667,42.4166666666667,'Python'),(-84.6,42.7833333333333,'Python'),(-93.2166666666667,44.8833333333333,'Python'),(-90.0833333333333,32.3166666666667,'Java'),(-94.5833333333333,39.1166666666667,'Java'),(-90.3833333333333,38.75,'Python'),(-108.533333333333,45.8,'Python'),(-95.9,41.3,'Python'),(-115.166666666667,36.0833333333333,'Java'),(-71.4333333333333,42.9333333333333,'R'),(-74.1666666666667,40.7,'R'),(-106.616666666667,35.05,'Python'),(-78.7333333333333,42.9333333333333,'R'),(-73.9666666666667,40.7833333333333,'R'),(-80.9333333333333,35.2166666666667,'Python'),(-78.7833333333333,35.8666666666667,'Python'),(-100.75,46.7666666666667,'Java'),(-84.5166666666667,39.15,'Java'),(-81.85,41.4,'Java'),(-82.8833333333333,40,'Java'),(-97.6,35.4,'Python'),(-122.666666666667,45.5333333333333,'Python'),(-75.25,39.8833333333333,'Python'),(-80.2166666666667,40.5,'Python'),(-71.4333333333333,41.7333333333333,'R'),(-81.1166666666667,33.95,'R'),(-96.7333333333333,43.5666666666667,'Python'),(-90,35.05,'R'),(-86.6833333333333,36.1166666666667,'R'),(-97.7,30.3,'Python'),(-96.85,32.85,'Java'),(-95.35,29.9666666666667,'Java'),(-98.4666666666667,29.5333333333333,'Java'),(-111.966666666667,40.7666666666667,'Python'),(-73.15,44.4666666666667,'R'),(-77.3333333333333,37.5,'Python'),(-122.3,47.5333333333333,'Python'),(-89.3333333333333,43.1333333333333,'R'),(-104.816666666667,41.15,'Java')]
# cities = [([longitude, latitude], language) for longitude, latitude, language in cities]

airquality = list(airq)
# airquality = [(3, 32, 'NORMAL_AIR'), (5, 52, 'NORMAL_AIR'), (4, 49, 'NORMAL_AIR'), (3, 34, 'NORMAL_AIR'), (3, 37, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (4, 47, 'NORMAL_AIR'), (4, 47, 'NORMAL_AIR'), (3, 0, 'NORMAL_AIR'), (4, 42, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (4, 44, 'NORMAL_AIR'), (4, 43, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (4, 47, 'NORMAL_AIR'), (4, 41, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (4, 41, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (3, 34, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (5, 53, 'NORMAL_AIR'), (4, 50, 'NORMAL_AIR'), (3, 34, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 37, 'NORMAL_AIR'), (4, 43, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (3, 23, 'NORMAL_AIR'), (4, 41, 'NORMAL_AIR'), (3, 32, 'NORMAL_AIR'), (4, 42, 'NORMAL_AIR'), (4, 43, 'NORMAL_AIR'), (4, 43, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (4, 42, 'NORMAL_AIR'), (4, 44, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (3, 36, 'NORMAL_AIR'), (3, 33, 'NORMAL_AIR'), (3, 31, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (2, 28, 'GOOD_AIR'), (3, 33, 'NORMAL_AIR'), (3, 33, 'NORMAL_AIR'), (2, 30, 'GOOD_AIR'), (3, 39, 'NORMAL_AIR'), (3, 40, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 33, 'NORMAL_AIR'), (3, 36, 'NORMAL_AIR'), (2, 30, 'GOOD_AIR'), (3, 34, 'NORMAL_AIR'), (3, 37, 'NORMAL_AIR'), (3, 37, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (3, 37, 'NORMAL_AIR'), (3, 34, 'NORMAL_AIR'), (3, 33, 'NORMAL_AIR'), (2, 30, 'GOOD_AIR'), (3, 39, 'NORMAL_AIR'), (3, 36, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (5, 55, 'NORMAL_AIR'), (5, 57, 'NORMAL_AIR'), (5, 52, 'NORMAL_AIR'), (3, 34, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (4, 42, 'NORMAL_AIR'), (4, 41, 'NORMAL_AIR'), (4, 49, 'NORMAL_AIR'), (4, 49, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (5, 61, 'NORMAL_AIR'), (4, 47, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (4, 47, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (5, 51, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (4, 43, 'NORMAL_AIR'), (4, 45, 'NORMAL_AIR'), (3, 38, 'NORMAL_AIR'), (4, 41, 'NORMAL_AIR'), (3, 39, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (5, 67, 'NORMAL_AIR'), (5, 65, 'NORMAL_AIR'), (5, 60, 'NORMAL_AIR'), (4, 46, 'NORMAL_AIR'), (5, 51, 'NORMAL_AIR'), (4, 49, 'NORMAL_AIR'), (4, 48, 'NORMAL_AIR'), (5, 53, 'NORMAL_AIR'), (5, 61, 'NORMAL_AIR'), (5, 61, 'NORMAL_AIR'), (5, 74, 'NORMAL_AIR'), (5, 63, 'NORMAL_AIR'), (5, 56, 'NORMAL_AIR'), (5, 65, 'NORMAL_AIR'), (5, 63, 'NORMAL_AIR'), (5, 65, 'NORMAL_AIR'), (5, 67, 'NORMAL_AIR'), (5, 59, 'NORMAL_AIR'), (5, 64, 'NORMAL_AIR'), (5, 55, 'NORMAL_AIR'), (5, 52, 'NORMAL_AIR'), (4, 50, 'NORMAL_AIR')] 
airquality = [([air_index, fdust], label) for air_index, fdust, label in airquality]

def plot_state_borders(plt, color='0.8'):
    pass

def plot_cities():

    # key is language, value is pair (longitudes, latitudes)
    plots = { "GOOD_AIR" : ([], []), "NORMAL_AIR" : ([], []), "BAD_AIR" : ([], []) }

    # we want each language to have a different marker and color
    markers = { "GOOD_AIR" : "o", "NORMAL_AIR" : "s", "BAD_AIR" : "^" }
    colors  = { "GOOD_AIR" : "r", "NORMAL_AIR" : "b", "BAD_AIR" : "g" }

    for (air_index, fdust), language in airquality:
        plots[GOOD_AIR][0].append(air_index)
        plots[label][1].append(fdust)

    # create a scatter series for each language
    for label, (x, y) in plots.items():
        plt.scatter(x, y, color = colors[language], marker = markers[label], label = label, zorder = 10)

    plot_state_borders(plt)    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location
    plt.axis([-130,-60,20,55]) # set the axes
    plt.title("AIR_CONDITION")
    plt.show()

def classify_and_plot_grid(k=1):
    plots = { "GOOD_AIR" : ([], []), "NORMAL_AIR" : ([], []), "BAD_AIR" : ([], []) }
    markers = { "GOOD_AIR" : "o", "NORMAL_AIR" : "s", "BAD_AIR" : "^" }
    colors  = { "GOOD_AIR" : "r", "NORMAL_AIR" : "b", "BAD_AIR" : "g" }

    for air_index in range(-130, -60):
        for fdust in range(20, 55):
            predicted_aircondition = knn_classify(k, airquality, [air_index, fdust])
            plots[predicted_aircondition][0].append(air_index)
            plots[predicted_aircondition][1].append(fdust)

    # create a scatter series for each language
    for label, (x, y) in plots.items():
        plt.scatter(x, y, color = colors[label], marker = markers[label], label = label, zorder = 0)

    plot_state_borders(plt, color = 'black')    # assume we have a function that does this

    plt.legend(loc = 0)          # let matplotlib choose the location
    plt.axis([-130, -60, 20, 55]) # set the axes
    plt.title(str(k) + "-Nearest Neighbor Programming Languages")
    plt.show()

#
# the curse of dimensionality
#

def random_point(dim):
    return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]

if __name__ == "__main__":
    predict = list()
    # try several different values for k
    for k in [3]:
        num_correct = 0

        for location, actual_aircondition in airquality:

            other_airs = [other_air
                            for other_air in airquality
                            if other_air != (location, actual_aircondition)]

            predicted_aircondition = knn_classify(k, other_airs, location)
            # print(predicted_aircondition)
            predict.append(predicted_aircondition)
            if predicted_aircondition == actual_aircondition:
                num_correct += 1

        print("K : ", k, "neighbor[s]:", num_correct, "correct out of", len(airquality))

tp = 0
tn = 0
fp = 0
fn = 0

# TP : 실제 TRUE, TRUE 라 예측
for i in range(len(airquality)) :
    if 1 <= airquality[i][0][0] <= 2 and 0 <= airquality[i][0][1] <= 15 and airquality[i][1] == predict[i] == 'GOOD_AIR' :
        tp += 1
    elif 3 <= airquality[i][0][0] <= 5 and 31 <= airquality[i][0][1] <=75 and airquality[i][1] == predict[i] == 'NORMAL_AIR' :
        tp += 1
    elif 6 <= airquality[i][0][0] <= 8 and 75 <= airquality[i][0][1] and airquality[i][1] == predict[i] == 'BAD_AIR' :
        tp += 1
print("TP : ", tp)

# TN : 실제 False, False 라 예측
for i in range(len(airquality)) :
    if 1 <= airquality[i][0][0] <= 2 and 0 <= airquality[i][0][1] <= 15 and airquality[i][1] == predict[i] == 'NORMAL_AIR' or 'BAD_AIR' :
        tn += 1
    elif 3 <= airquality[i][0][0] <= 5 and 31 <= airquality[i][0][1] <=75 and airquality[i][1] == predict[i] == 'GOOD_AIR' or 'BAD_AIR' :
        tn += 1
    elif 6 <= airquality[i][0][0] <= 8 and 75 <= airquality[i][0][1] and airquality[i][1] == predict[i] == 'GOOD_AIR' or 'NORMAL_AIR':
        tn += 1
print("TN : ", tn)

# FP : 실제 False, True 라 예측
for i in range(len(airquality)) :
    if 3 <= airquality[i][0][0] and 16 <= airquality[i][0][1] and airquality[i][1] == predict[i] == 'GOOD_AIR' :
        fp += 1
    elif 1 <= airquality[i][0][0] <= 4 and 7 <= airquality[i][0][0] and 0 <= airquality[i][0][1] <= 15 and 75 <= airquality[i][0][1] and airquality[i][1] == predict[i] == 'NORMAL_AIR' :
        fp += 1
    elif airquality[i][0][0] <= 7 and airquality[i][0][1] <= 74 and airquality[i][1] == predict[i] == 'BAD_AIR' :
        fp += 1
print("FP : ", fp)

# FN : 실제 False, False 라 예측
for i in range(len(airquality)) :
    if 3 <= airquality[i][0][0] and 16 <= airquality[i][0][1] and airquality[i][1]== predict[i] == 'NORMAL_AIR' or 'BAD_AIR' :
        fn += 1
    elif 1 <= airquality[i][0][0] <= 4 and 7 <= airquality[i][0][0] and 0 <= airquality[i][0][1] <= 15 and 75 <= airquality[i][0][1] and airquality[i][1] == predict[i] == 'GOOD_AIR' or 'BAD_AIR' :
        fn += 1
    elif airquality[i][0][0] <= 7 and airquality[i][0][1] <= 74 and airquality[i][1] == predict[i] == 'GOOD_AIR' or 'NORMAL_AIR' :
        fn += 1
print("FN : ", fn)

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f_score = 2 * precision * recall / (precision + recall)

# print("accuracy ", accuracy)
print("precision ", precision)
print("recall ", recall)
print("f-score", f_score)