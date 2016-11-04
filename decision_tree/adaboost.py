# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import decision_tree
import math
from sklearn import preprocessing

class Adaboost():
    
    def __init__(self, base_CLS, cls_num, parameters=None):
        if parameters is None:
            parameters = {}
        self.base_CLS = base_CLS
        self.cls_num = cls_num
        self.parameters = parameters
        self.cls_weights = []
        self.clss = []
    
    def predict(self, e):
        predict_labels = {}
        for index, cls in enumerate(self.clss):
            pl = cls.predict(e)
            if predict_labels.has_key(pl):
                predict_labels[pl] += self.cls_weights[index]
            else:
                predict_labels[pl] = self.cls_weights[index]
        key = max([key for key in predict_labels],
                  key=lambda x:predict_labels[x])
        return key

    def fit(self, examples, labels):
        len_D = len(labels)
        weights = [float(1) / len_D for e in examples]
        for i in range(self.cls_num):
            cls = self.base_CLS(**self.parameters)
            cls.fit(examples, labels)
            self.clss.append(cls)
            error = 0
            p_labels = []
            for index, e in enumerate(examples):
                p_label = cls.predict(e)
                p_labels.append(p_label)
                if p_label != labels[index]:
                    error += weights[index]
            error = max(float(error) / len_D, 0.0001)
            a = 0.5 * math.log((1 - error)/error, math.e)
            self.cls_weights.append(a)
            for index, pl in enumerate(p_labels):
                if pl == labels[index]:
                    weights[index] = weights[index] * math.e ** (-a)
                else:
                    weights[index] = weights[index] * math.e ** a
            sum_weight = sum(weights)
            weights = map(lambda x: x/sum_weight, weights)

if __name__ == '__main__':
    pass

