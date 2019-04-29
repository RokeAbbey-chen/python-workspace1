# -*- coding:utf-8 -*-
import math
import re

rp = re.compile("[\t ]")


def dist(x1, x2):
    return math.sqrt(sum((x1[i] - x2[i]) ** 2 for i in xrange(0, len(x1))))


def getNeighborsCount(xs, x0, r):
    return len(getNeighbors(xs, x0, r))


def getNeighbors(xs, x0, r):
    l = list()
    set((l.append(x) if dist(x, x0) <= r else None for x in xs))
    return l




def train(xs, minpts, r):
    """
    :param xs: 样本集合
    :param minpts: r邻域的向量数量
    :param r: r邻域的距离阈值
    :return:
    """
    stack = list()
    cluster = list()
    neighbors = dict()
    for x in xs:
        nbs = getNeighbors(xs, x, r)
        nbsc = len(nbs)
        if nbsc >= minpts:
            stack.append(x)
            neighbors.


    while len(stack) >= 0:
        clu = list()
        o = stack.pop()
        nbs = getNeighbors(xs, o, r)
        if len(nbs) >= minpts:
            clu.append(*nbs)

        for c in clu:
            getNe








def main():
    train_file = './test1.dat'
    minpts = 10
    r = 20
    train_data = list()
    with open(train_file, 'r') as f:
        for line in f:
            l = [int(s.replace('\n', '')) for s in rp.split(line)]
            l[0] = 0
            s = sum(l)
            l = [float(i) / s for i in l]
            train_data.append(l)

    train(train_data, minpts, r)



