# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import gain_tools
from node import Node
import gini_tools
import mce_tools

class Attribute_Node(Node):

    def split(self):
        if self.split_method == "gain":
            split_index = self.get_max_gain_index()
        elif self.split_method == "gini":
            split_index = self.get_max_gini_index()
        elif self.split_method == "mce":
            split_index = self.get_max_mce_index()
        self.split_index = split_index
        attribute_types = set([e[split_index] for e in self.examples])
        sub_examples = {}
        sub_labels = {}
        for index, example in enumerate(self.examples):
            if sub_examples.has_key(example[split_index]):
                sub_examples[example[split_index]].append(example)
                sub_labels[example[split_index]].append(self.labels[index])
            else:
                sub_examples[example[split_index]] = [example]
                sub_labels[example[split_index]] = [self.labels[index]]
        new_use_indexs = [index for index in self.use_indexs if index != split_index]
        for key in sub_examples:
            self.sons[key] = Attribute_Node(sub_examples[key],
                                            new_use_indexs,
                                            sub_labels[key],
                                            self.split_method)
    
    def get_max_gain_index(self):
        return self.get_max_index(gain_tools.gain)

    def get_max_gini_index(self):
        return self.get_max_index(gini_tools.gini_gain)

    def get_max_mce_index(self):
        return self.get_max_index(mce_tools.mce_gain)

    def get_max_index(self, gain_func):
        max_gain_index = None
        max_gain = -999999
        for index in self.use_indexs:
            gain = gain_func(self.examples,
                             index,
                             self.labels)
            if gain > max_gain:
                max_gain_index = index
                max_gain = gain
        assert max_gain_index != None
        return max_gain_index
   
    def predict(self, example):
        if self.label is None:
            attribute = example[self.split_index]
            if not self.sons.has_key(attribute):
                return self.most_label
            return self.sons[attribute].predict(example)
        else:
            return self.label

if __name__ == '__main__':
    pass

