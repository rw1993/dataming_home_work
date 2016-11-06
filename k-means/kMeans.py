# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import random
import tools
import numpy


class KMeans(object):

    def __init__(self, k, convergence=0):
        self.k = k
        self.convergence = convergence

    @property
    def SSE(self):
        subset = {}
        for i in range(len(self.centers)):
            subset[i] = []
        for example in self.examples:
            index = tools.find_nearest(example, self.centers)
            subset[i].append(example)
        sse = 0
        for key in subset:
            es = subset[key]
            for e in es:
                nc = numpy.array(self.centers[key])
                ne = numpy.array(e)
                nsse = (nc - ne) * (nc - ne)
                sse += nsse.sum()
        return sse


    def fit(self, examples):
        # init centers
        self.examples = examples
        max_range = max(map(max, examples))
        min_range = min(map(min, examples))
        lenth = len(examples[0])
        def get_rangdom():
            c = []
            for i in range(lenth):
                c.append(random.randrange(min_range, max_range,
                                          _int=float))
            return c
        centers = [get_rangdom() for i in range(self.k)]

        while True:
            ifchange = False
            subset = {}
            for i in range(len(centers)):
                subset[i] = []
            # split
            for e in examples:
                index = tools.find_nearest(e, centers)
                subset[index].append(e)
            # new center
            new_centers = []
            for i in range(len(centers)):
                if len(subset[i]) == 0:
                    continue # basic k-means
                nc = tools.get_centers(subset[i])
                new_centers.append(nc)
            if len(new_centers) != len(centers):
                centers = new_centers
                continue
            if self.ifchange(new_centers, centers):
                centers = new_centers
                break
            centers = new_centers
        self.centers = centers

    def ifchange(self, new_centers, old_centers):
        for nc, oc in zip(new_centers, old_centers):
            for n1, n2 in zip(nc, oc):
                if abs(n1 - n2) > self.convergence:
                    return True
        else:
             return False

if __name__ == '__main__':
    pass

