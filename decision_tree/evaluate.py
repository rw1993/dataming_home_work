# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import random
import decision_tree
import car_data
import iris_data
import wine_data
import numpy
import adaboost


def ten_fold(cls, examples, labels):
    d = {key:[] for key in range(10)}
    total_num = len(examples)
    each = float(total_num) / 10
    for index, example in enumerate(examples):
        indexs = [key for key in d if len(d[key]) < each]
        if len(indexs) >= 1:
            r_index = random.choice(indexs)
        else:
            r_index = random.choice([key for key in d])
        d[r_index].append(index)
    reults = []
    for key in d:
        train_examples = []
        train_labels = []
        test_labels = []
        test_examples = []
        for index in d[key]:
            test_labels.append(labels[index])
            test_examples.append(examples[index])
        for k in d:
            if k == key:
                continue
            for index in d[k]:
                train_examples.append(examples[index])
                train_labels.append(labels[index])
        cls.fit(train_examples, train_labels)
        reults.append(right_percent(cls, test_examples, test_labels))
    return numpy.average(numpy.array(reults))


def holdout(cls, examples, labels, percent=0.7):
    train_set_num = int(len(examples) * percent)
    test_set_num = len(examples) - train_set_num
    test_indexs = random.sample([i for i in range(len(examples))],
                                 test_set_num)
    train_examples = []
    test_examples = []
    train_labels = []
    test_labels = []
    for index, example in enumerate(examples):
        if index in test_indexs:
            test_examples.append(example)
            test_labels.append(labels[index])
        else:
            train_examples.append(example)
            train_labels.append(labels[index])
    cls.fit(train_examples, train_labels)
    return right_percent(cls, test_examples, test_labels)

def right_percent(cls, test_examples, test_labels):
    right = 0
    wrong = 0
    for index, example in enumerate(test_examples):
        if cls.predict(example) == test_labels[index]:
            right += 1
        else:
            wrong += 1
    return float(right) / (wrong + right)
    
def bootstrap(cls, examples, labels):
    indexs = [index for index, e in enumerate(examples)]
    train_labels = []
    train_examples = []
    for e in examples:
        index = random.choice(indexs)
        train_labels.append(labels[index])
        train_examples.append(examples[index])
    cls.fit(train_examples, train_labels)
    return right_percent(cls, examples, labels)
        


if __name__ == '__main__':
    cls = decision_tree.Decision_Tree()
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = decision_tree.Decision_Tree(attribute="continous")
    examples, labels = iris_data.read_iris_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    examples, labels = wine_data.get_wine_data()
    cls = decision_tree.Decision_Tree(attribute="continous")
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = decision_tree.Decision_Tree(split_method="mce")
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = decision_tree.Decision_Tree(split_method="gini")
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = decision_tree.Decision_Tree(pruning_method="post",
                                      pruning_rate=0.8)
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = decision_tree.Decision_Tree(pruning_method="pre",
                                      pruning_rate=0.8)
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
    cls = adaboost.Adaboost(decision_tree.Decision_Tree,
                            5)
    examples, labels = car_data.read_car_data()
    print holdout(cls, examples, labels)
    print ten_fold(cls, examples, labels)
    print bootstrap(cls, examples, labels)
