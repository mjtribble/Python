import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def euclidean_distance(row):
    """
    A simple euclidean distance function
    """
    fold1 = [(0.1, 0.7), (0.9, 0.2), (0.6, 0.6), (0.2, 0.8), (0.6, 0.3)]
    fold2 = [(0.9, 0.4), (0.3, 0.1), (0.1, 0.3), (0.3, 0.9), (0.7, 0.5)]
    fold3 = [(0.3, 0.3), (0.8, 0.6), (0.1, 0.1), (0.9, 0.8), (0.5, 0.7)]
    fold4 = [(0.7, 0.7), (0.7, 0.9), (0.4, 0.4), (0.7, 0.1), (0.3, 0.6)]
    fold5 = [(0.1, 0.9), (0.8, 0.5), (0.5, 0.9), (0.8, 0.1), (0.2, 0.5)]

    for point in fold1:
        min_distance = euclidean_distance(point, fold2) \
                       + euclidean_distance(point, fold3) \
                       + euclidean_distance(point, fold4) \
                       + euclidean_distance(point, fold5)

    inner_value = 0
    for i in row:
        inner_value += (row[i] - point) ** 2
    return np.math.sqrt(inner_value)
