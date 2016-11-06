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
        
             
def plot_best_k(examples):
    es = numpy.array(examples)
    sses = []
    for k in range(1, 10):
        subset = collections.defaultdict(list) 
        km = KMeans(n_clusters=k)
        km.fit(es)
        for e in examples:
            subset[km.predict(e)[0]].append(e)
        diameter = 0.0
        for key in subset:
            diameter = max(cluster_diameter(subset[key]),
                           diameter)
        print diameter
        sses.append(diameter)

    pyplot.plot([i for i in range(1, 10)], sses)
    pyplot.show()


examples, labels = iris_data.read_iris_data()
plot_best_k(examples)
examples, labels = wine_data.get_wine_data()
plot_best_k(examples)
