# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import sklearn.preprocessing as pre
import numpy


def read_continous_data(dataname="iris.data"):
    examples = []
    labels = []
    with open(dataname, "r") as f:
        for line in f.readlines():
            line = line.strip()
            e = line.split(",")
            labels.append(e[-1])
            examples.append(map(float, e[:-1]))
    examples = pre.normalize(numpy.array(examples))
    examples = [list(e) for e in examples]
    return examples, labels


def read_iris_data():
    return read_continous_data()


if __name__ == '__main__':
    examples, labels = read_iris_data()
    print labels, examples

