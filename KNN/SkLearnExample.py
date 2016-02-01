# -*- coding=utf-8 -*-

from sklearn import neighbors
from sklearn import datasets

__author__ = 'Ninlgde'

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

print iris

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([0.1, 0.2, 0.3, 0.4])

print predictedLabel

# with open('iris.data.txt', 'w') as f:
#     i = 0
#     for x in iris.data:
#         x = list(x)
#         x.append(iris.target_names[iris.target[i]])
#         for item in x:
#             f.write(str(item)+',')
#         f.write('\n')
#         i += 1
