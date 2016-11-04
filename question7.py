# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com


def read_table7():
    examples = []
    with open("table7", "r") as f:
        for line in f.readlines():
            line = line[:-1]
            example = line.split()
            label = example[-1]
            e = {}
            e['label'] = label
            e['feature'] = example[:-1]
            examples.append(e)
    return examples
'''
def count_percent(feature_index, feature, label, examples):
    total_num = 0
    feature_count = 0
    for e in examples:
        if e['label'] == label:
            total_num += 1
            if e['feature'][feature_index] == feature:
                feature_count += 1
    print total_num, feature_count
    return float(feature_count) / total_num
'''
def count_percent(feature_index, feature, label, examples):
    total_num = 0
    feature_count = 0
    for e in examples:
        if e['label'] == label:
            total_num += 1
            if e['feature'][feature_index] == feature:
                feature_count += 1
    return float(feature_count + 2) / (total_num+4)


if __name__ == '__main__':
    examples = read_table7()
    print count_percent(0, '1', '1', examples)
    print count_percent(1, '1', '1', examples)
    print count_percent(2, '1', '1', examples)
    print count_percent(0, '1', '0', examples)
    print count_percent(1, '1', '0', examples)
    print count_percent(2, '1', '0', examples)
