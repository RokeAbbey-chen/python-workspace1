# -*- coding:utf-8 -*-
import re
import numpy as np


def main():
    file_name = 'data.dat'
    elo_step = 50
    xs = list()
    p = re.compile('[\t ]+')
    mi_elo = 0x7FFFFFFF
    mx_elo = -0x7FFFFFFF
    with open(file_name) as f:
        for line in f:
            l = [float(s.replace('\n', '')) for s in p.split(line)]
            xs.append(l)
            mi_elo = min(mi_elo, l[0])
            mx_elo = max(mx_elo, l[0])

    def cmpf1(o1, o2):
        if o1[0] < o2[0]:
            return -1
        if o1[0] > o2[0]:
            return 1
        return 0

    xs = sorted(xs, cmp=cmpf1)
    mi_elo = int(mi_elo) / elo_step * elo_step
    new_xs = list()
    t = list()

    su = 0
    n = 0

    mi_elo2 = mi_elo
    print mi_elo, mx_elo

    xs.append([0x7fffffff, 0x7fffffff])
    for x in xs:
        if x[0] <= mi_elo + elo_step:
            t.extend(x[1:])
            n += 1
            su += x[0]
            print x[0], n, su / n
        else:
            # print '--------------'
            t = sorted(t)
            lt = len(t)
            # for i in xrange(int(lt * 0.1)):
            #     t.pop()
            left_lt = lt * 0.7
            if left_lt > 10:
                for i in xrange(int(lt - left_lt) - 1, -1, -1):
                    del t[i]

            new_xs.append(t)
            t = x[1:]
            su = x[0]
            n = 1
            print x[0], n, su / n
            print 'mi_elo = {}, mx_elo = {}'.format(mi_elo, mx_elo)
            mi_elo += elo_step
            if mi_elo > mx_elo:
                print 'break!!!'
                break

    mi_elo = mi_elo2
    with open('out.dat', 'w') as f:
        for x in new_xs:
            f.write('{} {} {}\n'.format(mi_elo, np.mean(x), np.std(x, ddof=1)))
            mi_elo += elo_step


if __name__ == '__main__':
    main()




b = []
from collections import OrderedDict

od = OrderedDict()
for i in b:
    if od.get(i, 0) > 0:
        od[i] += 1
    else:
        od.setdefault(i, 1)
