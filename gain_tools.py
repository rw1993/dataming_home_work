# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import math


def entropy(labels):
    labels_set = set(labels)
    return sum([label_entropy(labels, l) for l in labels_set])


def label_entropy(labels, label):
    total = len(labels)
    this_label = len([l for l in labels if l == label])
    percent = float(this_label) / float(total)
    return -percent * math.log(percent, 2)

def read_lables(name):
    labels = []
    with open(name, "r") as f:
        for line in f.readlines():
            line = line[:-1]
            labels.append(line)
    return labels

def read_examples(name):
    examples = []
    with open(name, "r") as f:
        for line in f.readlines():
            line = line[:-1]
            #print line
            example = line.split(",")
            examples.append(example)
    return examples


def continous_attribute_gain(examples, attribute_index, labels):
    before = entropy(labels)
    total_num = len(labels)
    values = [example[attribute_index] for example in examples]
    values = map(float, values)
    values = set(values)
    values = sorted(list(values))
    split_values = []
    for index, value in enumerate(values):
        if index == len(values) - 1:
            pass
        else:
            split_value = values[index+1] + value
            split_value /= 2
            split_values.append(split_value)
    splits = []
    for split_value in split_values:
        bigger = []
        less = []
        for index, example in enumerate(examples):
            value = float(example[attribute_index])
            if value > split_value:
                bigger.append(labels[index])
            else:
                less.append(labels[index])
        after = [entropy(less), entropy(bigger)]
        percents = [float(len(less))/total_num,
                    float(len(bigger))/total_num]
        after = sum(map(lambda x, y: x*y, after, percents))
        splits.append(before - after)
    return zip(split_values, splits)


def gain(examples, attribute_index, labels):
    before = entropy(labels)
    #print before
    subset = {}
    total_num = len(labels)
    for index, example in enumerate(examples):
        attribute = example[attribute_index]
        if subset.has_key(attribute):
            subset[attribute].append(labels[index])
        else:
            subset[attribute] = [labels[index]]
    #print subset
    entropys = [entropy(subset[key]) for key in subset]
    after = 0
    percents = [float(len(subset[key]))/float(total_num) for key in subset]
    for index, e in enumerate(entropys):
        after += percents[index] * e
    #print after
    return before - after, subset


def gain_ratio(examples, attribute_index, labels):
    gain_, subset = gain(examples, attribute_index, labels)
    percents = [len(subset[key]) for key in subset]
    percents = [float(p) / len(labels) for p in percents]
    percents = map(lambda p: -p*math.log(p, 2), percents)
    down = sum(percents)
    return gain_ / down

def label_gini(labels):
    lebel_set = set(labels)
    gini = 0
    for lebel in lebel_set:
        p = len([l for l in labels if l == lebel])
        p = float(p) / len(labels)
        gini +=  p**2
    return 1 - gini

def attribute_gini(examples, attribute_index):
    lebels = [example[attribute_index] for example in examples]
    return label_gini(lebels)
        
        

        
if __name__ == '__main__':
    labels = read_lables("lable1")
    examples = read_examples("table1")
    #print examples
    #print label_entropy(labels, "1")
    #print entropy(labels)
    print gain_ratio(examples, 1, labels)
    print gain_ratio(examples, 2, labels)
    print attribute_gini(examples, 0)
    print continous_attribute_gain(examples, 3, labels)
