# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import iris_data
import wine_data
from sklearn.cluster import KMeans
from matplotlib import pyplot
import numpy
import collections

def cluster_diameter(es):
    es = numpy.array(es)
    maybe = []
    for index, e in enumerate(es):
        for index1, e2 in enumerate(es):
             if index1 > index:
                 maybe.append((e, e2))
    max_ = 0
    for e1, e2 in maybe:
        diameter = (e1 - e2) * (e1 - e2)
        diameter = diameter.sum() ** 0.5
        max_ = max(diameter, max_)
    return max_
        
             
def plot_best_k(examples, km):
    es = numpy.array(examples)
    sses = []
    subset = collections.defaultdict(list) 
    km.fit(es)
    for e in examples:
        subset[km.predict(e)[0]].append(e)
    diameter = 0.0
    for key in subset:
        diameter = max(cluster_diameter(subset[key]),
                       diameter)
    print diameter

if __name__ == "__main__":
    """
    examples, labels = iris_data.read_iris_data()
    plot_best_k(examples)
    examples, labels = wine_data.get_wine_data()
    plot_best_k(examples)
    """
    examples, labels = iris_data.read_iris_data()
    km = KMeans(n_clusters=2, init="k-means++")
    plot_best_k(examples, km)
    km = KMeans(n_clusters=2, init="random")
    plot_best_k(examples, km)
    km = KMeans(n_clusters=2, init=numpy.array([[1000, 1000, 1000, 1000], 
                                               [-1000,-1000, 1000, 1000]]))
    plot_best_k(examples, km)
