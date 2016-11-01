# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import collections

def class_error_rate(labels):
    counter =  collections.defaultdict(int)
    for l in labels:
        counter[l] += 1
    max_key = None
    for key in counter:
        if max_key is None:
            max_key = key
        elif counter[max_key] < counter[key]:
            max_key = key
    p = 1 - float(counter[max_key]) / len(labels)
    return key, counter[max_key], p

def error_rate_after
if __name__ == '__main__':
    print class_error_rate([0,1,1,1,1,1])

