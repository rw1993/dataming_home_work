# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
from node import Node
import gain_tools


class Continous_Node(Node):
    def predict(self, example):
        if self.label is  not None:
            return self.label
        attribute = example[self.split_index]
        if attribute > self.split_value:
            return self.sons["bigger"].predict(example)
        else:
            return self.sons["smaller"].predict(example)

    def split(self):
        split_value, split_index = self.get_max_index()
        self.split_value = split_value
        self.split_index = split_index
        #new_use_indexs = [index for index in self.use_indexs if index != split_index]
        bigger_examples = []
        bigger_labels = []
        smaller_examples = []
        smaller_labels = []
        for index, e in enumerate(self.examples):
            if e[split_index] > split_value:
                l = bigger_labels
                es = bigger_examples
            else:
                l = smaller_labels
                es = smaller_examples
            l.append(self.labels[index])
            es.append(self.examples[index])
        if len(bigger_labels) == 0 or len(smaller_labels) == 0:
            self.label = self.most_label
            return 
        self.sons["bigger"] = Continous_Node(bigger_examples,
                                             self.use_indexs,
                                             bigger_labels)
        self.sons["smaller"] = Continous_Node(smaller_examples,
                                              self.use_indexs,
                                              smaller_labels)

    def get_max_index(self):
        max_gain = 0
        split_value = None
        split_index = None
        for attribute in self.use_indexs:
            splits = gain_tools.continous_attribute_gain(self.examples,
                                                         attribute,
                                                         self.labels)
            if not splits:
                continue
            splits = sorted(splits, key=lambda x:x[1])
            split = splits[0]
            assert len(split) == 2
            if split_value is None:
                split_value = split[0]
                max_gain = split[1]
                split_index = attribute
            elif max_gain < split[0]:
                split_value = split[0]
                max_gain = split[1]
                split_index = attribute
        return split_value, split_index
