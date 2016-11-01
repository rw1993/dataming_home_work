# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import error_rate_tools
def readtable2():
    examples =[]
    labels = []
    with open("table2", "r") as f:
        for line in f.readlines():
            line = line[:-1]
            example = line.split()
            label = example[-2]
            num = int(example[-1])
            print num
            example = example[:-2]
            examples += [example]*num
            labels += [label]*num
    return examples, labels
if __name__ == '__main__':
    examples, labels = readtable2()

