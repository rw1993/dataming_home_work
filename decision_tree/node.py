# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import collections


class Node(object):

    def prune(self):
        count_label = self.count_label
        if self.label is not None:
            return
        if float(count_label[self.most_label]) / len(self.labels) > self.pruning_rate:
            self.label = self.most_label
            return
        for key in self.sons:
            self.sons[key].prune()

    def __init__(self, examples, use_indexs, labels, split_method="gain",
                 pruning_method=None, pruning_rate=None):
        self.label = None
        self.examples = examples
        self.use_indexs = use_indexs
        self.labels = labels
        self.split_method = split_method
        self.pruning_method = pruning_method
        self.pruning_rate = pruning_rate
        self.count_label = collections.defaultdict(int)
        count_label = self.count_label
        for label in labels:
            count_label[label] += 1
        self.most_label = max(count_label.keys(),
                              key=lambda x:count_label[x])
        if self.pruning_method == "pre":
            if float(count_label[self.most_label]) / len(labels) > self.pruning_rate:
                self.label = self.most_label
                return
        labels_set = set(labels)
        if len(labels_set) == 1:
            self.label = labels[0]
            return
        self.sons = {}
        self.split()

    @classmethod
    def root_node(cls, examples, labels, split_method, pruning_method,
                  pruning_rate):
        use_indexs = [index for index, attr in enumerate(examples[0])]
        return cls(examples, use_indexs, labels, split_method,
                   pruning_method, pruning_rate)




if __name__ == '__main__':
    pass

