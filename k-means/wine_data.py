# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import sklearn.preprocessing as pre
import numpy


def get_wine_data():
    examples =  []
    labels = []
    with open("wine.data", "r") as f:
        for line in f.readlines():
            line = line.strip()
            e = line.split(",")
            l = e[0]
            e = e[1:]
            e = map(float, e)
            examples.append(e)
            labels.append(l)
    examples = pre.maxabs_scale(numpy.array(examples))
    return examples, labels

if __name__ == '__main__':
    examples, labels = get_wine_data()
    print examples

