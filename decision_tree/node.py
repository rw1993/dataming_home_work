# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import collections


class Node(object):
    def __init__(self, examples, use_indexs, labels, split_method="gain"):
        self.label = None
        self.examples = examples
        self.use_indexs = use_indexs
        self.labels = labels
        self.split_method = split_method
        count_label = collections.defaultdict(int)
        for label in labels:
            count_label[label] += 1
        self.most_label = max(count_label.keys(),
                              key=lambda x:count_label[x])
            
        labels_set = set(labels)
        if len(labels_set) == 1:
            self.label = labels[0]
            return
        self.sons = {}
        self.split()

    @classmethod
    def root_node(cls, examples, labels, split_method):
        use_indexs = [index for index, attr in enumerate(examples[0])]
        return cls(examples, use_indexs, labels, split_method)




if __name__ == '__main__':
    pass

