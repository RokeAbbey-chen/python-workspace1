# -*- coding:utf-8 -*-
from math import exp
import re
import pprint as pp

precision = 0.001


def p1(w, x):
    """
    计算p1
    :param w:
    :param x:
    :return:
    """
    return 1.0 / (1 + exp(- sum((w[i] * x[i] for i in xrange(len(w))))))


def p0(w, x):
    """
    计算p0
    :param w:
    :param x:
    :return:
    """
    return 1 - p1(w, x)


def fw_1(w, xs, ys):
    """
    计算对数似然函数的一阶导数, 需要注意的是fw_1的计算结果是个向量
    :param w: 当前权重向量
    :param xs: 样本集合
    :param ys: 标记集合
    :return: 结果向量
    """
    result = list((0 for i in xrange(len(w))))
    for k in xrange(len(xs)):
        xi = xs[k]
        yi = ys[k]
        p_0 = p0(w, xi)
        for i in xrange(len(result)):
            result[i] += -xi[i] * p_0 + (1 - yi) * xi[i]
            # if i == 0:
            #     print 'result[0] = {}, p_0 = {}, xi[0] = {}, yi = {}'.format(result[i], p_0, xi[0], yi)

    return result


def fw_2(w, xs):
    """
    计算对数似然函数的二阶导数
    :param w: 权重向量
    :param xs: 变量集合
    :return: 结果值
    """
    s = 0
    for i in xrange(len(xs)):
        p_1 = p1(w, xs[i])
        p_0 = p0(w, xs[i])
        s += sum(xs[i][j] ** 2 * p_1 * p_0 for j in xrange(len(xs[i])))
        # s += sum((xs[i][j] ** 2) * p_1 * p_0 for j in xrange(1))
    return s


def update_w(wn, xs, ys):
    """
    以牛顿法更新w
    :param wn: 旧的w
    :param xs: 样本集合
    :param ys: 标记集合
    :return: 新的w, 以及是否应该停止迭代，true表示应该停止，false表示应该继续
    """
    r_1 = fw_1(wn, xs, ys)
    r_2 = fw_2(wn, xs)
    stop = True
    for i in r_1:
        stop = stop and abs(i) <= precision
    print 'r_1 : {}, r_2 : {}'.format(r_1, r_2)
    return [wn[i] - r_1[i] / r_2 for i in xrange(len(wn))], stop


def load(dat, normalize=False):
    xs = list()
    ys = list()
    p = re.compile(u'[\t ]+')
    with open(dat) as f:
        for line in f:
            l = [float(s.replace('\n', '')) for s in p.split(line)]
            ys.append(l[-1])
            l[-1] = 1
            xs.append(l)
    if normalize:
        xs_t = zip(*xs)
        maxs = [max(x_t) for x_t in xs_t]
        mins = [min(x_t) for x_t in xs_t]
        xs_new = [[(xi[j] - mins[j]) * 1.0 / (maxs[j] - mins[j]) if maxs[j] != mins[j] else 1 for j in xrange(len(maxs))] for xi in xs]
        xs = xs_new

    return xs, ys


def train(xs, ys):
    wn = [0 for i in xrange(len(xs[0]))]
    stop = False
    while not stop:
        wplus, stop = update_w(wn, xs, ys)
        wn = wplus
        print 'wplus : {}'.format(wplus)
    return wplus


def sigmoid(w, x):
    return 1.0 / (1 + exp(- sum(w[i] * x[i] for i in xrange(len(w)))))


def test(xs, ys, w):
    cc = 0
    wc = 0
    cx = list()
    wx = list()
    for i in xrange(len(xs)):
        xi = xs[i]
        y = round(sigmoid(w, xi))
        if y == ys[i]:
            cc += 1
            cx.append(xi)
        else:
            wc += 1
            wx.append(xi)

    print "权重向量w = {}".format(w)
    print "测试样本数量为: {}, 正确分类样本数量为{}, 错误样本数量为{}, 正确率为{}".format(len(xs), cc, wc, cc * 1.0 / len(xs))
    print "错误分类样本集\n{}".format(pp.pformat(wx))
    print "正确分类样本集\n{}".format(pp.pformat(cx))


def equal(x1, x2):
    for i in xrange(len(x1)):
        if abs(x1[i] - x2[i]) >= precision:
            return False
    return True


def main():
    """
    分类标记请使用1 0
    :return:
    """
    train_file = u'./train.dat'
    test_file = u'./test1.dat'
    xs, ys = load(train_file, True)
    txs, tys = load(test_file, True)
    print u'开始训练'
    w = train(xs, ys)
    # w = [366.1297055756627, 512.746530053357, -437.70654288790354]
    print u'开始判断'
    test(txs, tys, w)


if __name__ == '__main__':
    main()







