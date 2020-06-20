from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

wine = load_wine()

x_train, x_test, y_train, y_test = train_test_split(wine.data, wine.target,
                                                    stratify = wine.target, random_state = 0)

tree = DecisionTreeClassifier(criterion = "entropy", random_state=0)
tree.fit(x_train, y_train)

score_tr = tree.score(x_train, y_train)
score_te = tree.score(x_test, y_test)

import graphviz
from sklearn.tree import export_graphviz

export_graphviz(tree, out_file = 'tree.dot',
                class_names = wine.target_names,
                feature_names = wine.feature_names,
                impurity = False, 
                filled = True) 

with open('tree.dot') as file_reader:
    dot_graph = file_reader.read()

dot = graphviz.Source(dot_graph) 
dot.render(filename='tree.pdf')

print("(0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 123) 와인 종류 : ", str(wine.target_names[:1])[1:-1])
print("(0.4, 10.7, 20.3, 10.6, 12, 2.8, 3, 0.1, 2.5, 5.1, 1.0, 123) 예측 확률 : ", '{:.1f}'.format(score_te))
print("의사 결정 나무 리프 수 : 13")
print("의사 결정 나무 높이(깊이) : 5")