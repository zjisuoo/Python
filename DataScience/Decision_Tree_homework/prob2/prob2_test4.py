from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
import numpy as np

wine = load_wine()
print(wine.keys())
print(wine.target)

x = wine.data[:, [2, 3]]
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1, straify = y)

def plot_decision_regisons(x, y, classifier, test_idx = None, resolution = 0.02) :
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = x[:, 0].min() -1, x[:, 0].max() + 1
    x2_min, x2_max = x[:, 0].min() -1, x[:, 0].max() + 1

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    z = classifier.predict(np.array*[xx1.ravel(), xx2.ravel()].T)
    z = z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, z, alpha = .3, cmap = cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)) :
        plt.scatter(x = x[y == cl, 0], y = x[y ==cl, 1], alpha = 0.8, c = colors[idx], marker = markers[idx], label = cl, edgecolors = "black")

    if test_idx :
        x_test, y_test = x[test_idx, :], y[test_idx]
        pkt.scatter(x_test[:, 0], x_test[:, 1], c = '', edgecolors = "black", alpha = 1.0, linewidth = 1, marker = "o", s = 100, label = "test set")

tree = DecisionTreeClassifier(criterion = "gini", max_depth = 4, random_state = 1)
tree.fit(x_train, y_train)

x_combined = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))

plot_decision_regisons(x_combined, y_combined, classifier = tree, test_idx = range(105, 150))
plt.show()
save_fig("wine_decision")

'''
wine.target[[10, 80, 140]]
print(wine.target[[10, 80, 140]])
print(list(wine.target_names))

print(cross_val_score(clf, wine.data, wine.target, cv=10))
'''