# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
def disition_tree(example):
    if example[0] == 0:
        if example[1] == 0:
            return 1
        else:
            return 0
    else:
        if example[2] == 0:
            return 1
        else:
            return 0
    assert True, "no result"

def get_tp(examples, labels):
    tp = 0
    for index, example in enumerate(examples):
        if labels[index] == disition_tree(example) == 1:
            tp += 1
    return tp
def get_fn(examples, labels):
    fn = 0
    for index, example in enumerate(examples):
        if labels[index] == 1:
            if disition_tree(example) == 0:
                fn += 1
    return fn
def get_fp(examples, labels):
    fp = 0
    for index, example in enumerate(examples):
        if labels[index] == 0:
            if disition_tree(example) == 1:
                fp += 1
    return fp
def get_tn(examples, labels):
    tn = 0
    for index, example in enumerate(examples):
        if labels[index] == disition_tree(example) == 0:
            tn += 1
    return tn


def read_table3():
    examples = []
    labels = []
    with open("table3", "r") as f:
        for line in f.readlines():
            example = line[:-1].split()
            example = map(int, example)
            label = example[-1]
            example = example[:-1]
            examples.append(example)
            labels.append(label)
    return examples, labels
def generalize_error(examples, labels):
    total = 0
    error = 0
    for index, example in enumerate(examples):
        total += 1
        if disition_tree(example) == labels[index]:
            continue
        error += 1
    return total, error, float(error) / total
        
if __name__ == '__main__':
    examples, labels = read_table3()
    print get_tp(examples[:10], labels)
    print get_fn(examples[:10], labels)
    print get_fp(examples[:10], labels)
    print get_tn(examples[:10], labels)
    print generalize_error(examples[10:], labels[10:])

