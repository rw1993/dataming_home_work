# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import gain_tools
import collections
from attribute_node import Attribute_Node
from continous_node import Continous_Node


class Decision_Tree(object):
    node_type_map = {"attribute": Attribute_Node,
                     "continous": Continous_Node}

    def __init__(self, split_method="gain", pruning_method=None,
                 attribute="attribute", pruning_rate=None):
        self.split_method = split_method
        self.pruning_method = pruning_method
        self.Node = self.node_type_map[attribute]
        self.pruning_rate = pruning_rate

    def fit(self, examples, labels):
        self.root = self.Node.root_node(examples, labels,
                                        self.split_method,
                                        self.pruning_method,
                                        self.pruning_rate)
        if self.pruning_method == "post":
            self.root.prune()
    
    def predict(self, example):
        assert not self.root is None, "predict before fit"
        return self.root.predict(example)



if __name__ == '__main__':
    pass

