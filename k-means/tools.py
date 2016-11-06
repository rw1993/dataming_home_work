# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import numpy



def find_nearest(example, centers):
    indexs = [i for i, c in enumerate(centers)]
    def key_func(i):
        c = centers[i]
        c = numpy.array(c)
        e = numpy.array(example)
        return numpy.linalg.norm(c-e)
    return min(indexs, key=key_func)

def get_centers(arrays):
    arrays = map(numpy.array, arrays)
    return sum(arrays) / len(arrays)
if __name__ == '__main__':
    pass

