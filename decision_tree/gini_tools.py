# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import collections


def gini(labels):
    counter = collections.Counter(labels)
    gini = 0.0
    for key in counter:
        label_num = counter[key]
        p = float(label_num) / len(labels)
        gini += p ** 2
    return 1 - gini

def gini_gain(examples, attribute_index, labels):
    subset = {}
    total_lenth = len(examples)
    before_gini = gini(labels)
    for index, e in enumerate(examples):
        attribute = e[attribute_index]
        if subset.has_key(attribute):
            subset[attribute][0].append(e)
            subset[attribute][1].append(labels[index])
        else:
            subset[attribute] = [[e], [labels[index]]]
    after_gini = 0.0
    for key in subset:
        g = gini(subset[key][1])
        after_gini += g * float(len(subset[key][1])) / total_lenth
    return before_gini - after_gini





if __name__ == '__main__':
    pass

