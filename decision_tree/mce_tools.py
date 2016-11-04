# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import collections


def mce(labels):
    counter = collections.Counter(labels)
    max_label = max([key for key in counter], key=lambda x: counter[key])
    return 1 - float(counter[max_label]) / len(labels)

def mce_gain(examples, attribute_index, labels):
    before_mcls = mce(labels)
    subset = {}
    for index, e in enumerate(examples):
        attribute = e[attribute_index]
        if subset.has_key(attribute):
            subset[attribute][0].append(e)
            subset[attribute][1].append(labels[index])
        else:
            subset[attribute] = [[e],[labels[index]]]
    after_mcls = 0.0
    for key in subset:
        g = mce(subset[attribute][1])
        after_mcls += g * float(len(subset[attribute][1])) / len(labels)
    return before_mcls - after_mcls
    

if __name__ == '__main__':
    pass

