# -*- coding:utf-8 -*-
import re
import random as rd
import functools

mx = [-0x7FFFFFFF, -0x7FFFFFFF, -0x7FFFFFFF]
mi = [0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF]

xrange = range
def max_min_normalization_init(xs):
    xrg = xrange(len(xs[0]))
    for x in xs:
        for j in xrg:
            mx[j] = max(mx[j], x[j])
            mi[j] = min(mi[j], x[j])
    for x in xs:
        for j in xrg:
            x[j] -= mi[j]
            x[j] /= mx[j] - mi[j]

    with open('max_min_normalization.dat', 'w') as f:
        f.write('max = {}\nmi = {}'.format(mx, mi))



def main():
    p = re.compile('[\t ]+')
    t = list()

    def cmpf(o1, o2):
        if o1[0] > o2[0] or o1[0] == o2[0] and o1[1] > o2[1]:
            return 1
        if o1[0] < o2[0] or o1[0] == o2[0] and o1[1] < o2[1]:
            return -1
        return 0

    with open(u'ord_train.dat', 'r+') as f:
        for line in f:
            l = [float(s.replace('\n', '')) for s in p.split(line)]
            l[1] = int(l[1]) / 5
            l[1] = float(min(l[1], 12))
            t.append(l)
    # t = sorted(t, cmp=cmpf)
    t = sorted(t, key=functools.cmp_to_key(cmpf))
    t.append([0x7FFFFFFF, 0x7FFFFFFF, 0x7FFFFFFF])  # 多加一条假数据可以修复下面循环最后一条数据不加入xs的bug
    print('t = {}'.format(t))

    su = t[0][2]
    cnt = 1
    xs = list()
    for i in xrange(1, len(t)):
        line = t[i]
        last_line = t[i-1]
        if line[0] != last_line[0] or line[1] != last_line[1]:
            x = [last_line[0], last_line[1], su / cnt]
            xs.append(x)
            cnt = 0
            su = 0
        su += line[2]
        cnt += 1
    print( 'xs = {}'.format(xs))
    max_min_normalization_init(xs)
    txs = rd.sample(xs, int(len(xs) / 10))

    with open('train.dat', 'w') as tr:
        with open('test.dat', 'w') as tst:
            for x in xs:
                line = '{}\t{}\t{}\n'.format(x[0], x[1], x[2])
                if x not in txs:
                    tr.write(line)
                else:
                    tst.write(line)


def show_real_result():
    mx = [1616.0, 10.0, 1781.0]
    mi = [1003.0, 0.0, 109.0]
    p = re.compile('[\t ]+')
    with open('test.dat', 'r') as f:
        with open('ord_test.dat', 'w') as rf:
            for line in f:
                s = p.split(line)
                l = '{} {} {}\n'.format(*[round(float(s[i].replace('\n', '')) * (mx[i] - mi[i]) + mi[i], 2) for i in xrange(len(s))])
                rf.write(l)


if __name__ == u'__main__':
    main()
    # show_real_result()