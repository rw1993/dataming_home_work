# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com


def read_car_data():
    examples = []
    labels = []
    with open("car.data", "r") as f:
        for line in f.readlines():
            example = line.strip().split(",")
            label = example[-1]
            example = example[:-1]
            examples.append(example)
            labels.append(label)
    return examples, labels

if __name__ == '__main__':
    examples, labels = read_car_data()
    print labels

