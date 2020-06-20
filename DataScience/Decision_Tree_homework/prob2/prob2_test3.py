import sklearn
from sklearn.datasets import load_wine
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import classification_report

wine = load_wine()
print(wine.feature_names)
print(wine.DESCR)

from typing import NamedTuple, Optional

class wine(NamedTuple):
    alcohol : str
    malic_acid : str
    ash : str
    alcalinity_of_ash : str
    magnesium : str
    total_phenols : str
    flavanoids : str
    nonflavanoid_phenols : str
    proanthocyanins : str
    color_intensity : str
    hue : str
    #od280/od315_of_diluted_wines : str
    proline : str
    
#X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size = 0.30, random_state = 0)
inputs = [wine(0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 123)]
#y_test = train[[0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 2.3, 123]]

from sklearn import tree
classifier = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5,splitter = 'random')
classifier = classifier.fit(X_train,y_train)

prediction = classifier.predict(X_test)

accuracy = sklearn.metrics.accuracy_score(prediction, y_test)
print("Accuracy: ", '%.2f'% (accuracy*100),"%")
# print(classifier([0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 2.3, 123]))

def build_tree_id3(inputs: List[Any],
                   split_attributes: List[str],
                   target_attribute: str) -> DecisionTree:
    # Count target labels
    label_counts = Counter(getattr(input, target_attribute)
                           for input in inputs)
    most_common_label = label_counts.most_common(1)[0][0]

    # If there's a unique label, predict it
    if len(label_counts) == 1:
        return Leaf(most_common_label)

    # If no split attributes left, return the majority label
    if not split_attributes:
        return Leaf(most_common_label)

    # Otherwise split by the best attrib

trees = build_tree_id3(inputs, ['alcohol',
                     'malic_acid',
                     'ash',
                     'alcalinity_of_ash',
                     'magnesium',
                     'total_phenols',
                     'flavanoids',
                     'nonflavanoid_phenols',
                     'proanthocyanins',
                     'color_intensity',
                     'hue',
                     'od280/od315_of_diluted_wines',
                     'proline'], classes)
# classifier = tree.DecisionTreeClassifier().fit(wine.data[train_index],dataset.target[train_index])
#predict = classifier.predict(dataset.data[test_index])
#dic={}
#accuracy = sklearn.metrics.accuracy_score(predict, dataset.target[test_index])
#     dic = globals()['sample%s' %i ] = accuracy *100
#     print(dic)
#dic[classifier] = accuracy*100
#trees.append(dic)
#A dictionary file output of each tree and the subsequent Accuracy score of the preidction
print(trees)

