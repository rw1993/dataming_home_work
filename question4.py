# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
def get_percents():
    percents = []
    labels = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0]
    assert len(labels) == 10
    with open("table4", "r") as f:
        for line in f.readlines():
            percent = float(line[:-1])
            percents.append(percent)
    return zip(percents, labels)

def TP(percents, threshold):
    tp = 0
    for p in percents:
        if p[1] == 1 and p[0] >= threshold:
            tp += 1
    return tp

def FN(percents, threshold):
    fn = 0
    for p in percents:
        if p[1] == 1 and p[0] < threshold:
            fn += 1
    return fn
def FP(percents, threshold):
    fp = 0
    for p in percents:
        if p[1] == 0 and p[0] >= threshold:
            fp += 1
    return fp
def TN(percents, threshold):
    tn = 0
    for p in percents:
        if p[1] == 0 and p[0] < threshold:
            tn += 1
    return tn

def TPR(percents, threshold):
    tp = TP(percents, threshold)
    fn  = FN(percents, threshold)
    return float(tp) / (tp+fn)

def FPR(percents, threshold):
    fp = FP(percents, threshold)
    tn = TN(percents, threshold)
    return float(fp) / (fp+tn)
def Recall(percents, threshold):
    tp = TP(percents, threshold)
    fn = FN(percents, threshold)
    return float(tp) / (tp + fn)
def Precision(percents, threshold):
    tp = TP(percents, threshold)
    fp = FP(percents, threshold)
    return float(tp) / (tp+fp)
if __name__ == '__main__':
    percents = sorted(get_percents(), reverse=True)
    for p in percents:
        tpr = TPR(percents, p[0])
        fpr = FPR(percents, p[0])
        print tpr, fpr
    print "done"
    for p in percents:
        precision = Precision(percents, p[0])
        recall = Recall(percents, p[0])
        print precision, recall

