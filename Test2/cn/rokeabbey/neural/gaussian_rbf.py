# -*- coding:utf-8 -*-
from math import exp
from math import sin
import re
import random as rd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

precision = 0.01

xrange = range


def matrix_add(m1, m2):
    # print( u'm1 = {}, m2 = {}'.format(m1, m2))
    if type(m1[0]) == list or type(m1[0]) == tuple:
        return [[m1[i][j] + m2[i][j] for j in xrange(len(m1[i]))] for i in xrange(len(m1))]
    else:
        return [m1[i] + m2[i] for i in xrange(len(m1))]


def gaussian_func(sigma_t, x, c_t):
    # print( "beta_t = {}, x = {}, c_t = {}".format(beta_t, x, c_t))
    return exp(-beta(sigma_t) * sum((x[i] - c_t[i]) ** 2 for i in xrange(len(x))))


def h(sigma_t, x, c_t):
    """计算隐层输出值"""
    return gaussian_func(sigma_t, x, c_t)


def delta_c(x, y, y_, w, sigma, c, eta):
    """
    :param x: 样本向量
    :param y: 标记向量
    :param y_: 预测结果向量
    :param w: 权重系数矩阵
    :param sigma: sigma向量
    :param c: 更新前的c矩阵
    :param eta: 学习率
    :return: delta c
    """
    # print( "x = {}, y = {}, y_ = {}, w = {}, sigma = {}, c = {}, eta = {}".format(x, y, y_, w, sigma, c, eta))
    result = list()
    for t in xrange(len(c)):
        h_t = h(sigma[t], x, c[t])
        result.append(
            [-eta * sum([(y_[j] - y[j]) * w[j][t] for j in xrange(len(y))]) * h_t * -2 * beta(sigma[t]) * (
                c[t][i] - x[i])
             for i in xrange(len(x))]
        )

    return result


def delta_w(x, y, y_, sigma, c, lmbda, w, eta):
    """
    求取w的增量
    :param x: 样本向量
    :param y:
    :param y_:
    :param sigma:
    :param c:
    :param lmbda:
    :param w:
    :param eta: 学习率
    :return:
    """
    result = [[-eta * (2 * lmbda * w[j][t] + (y_[j] - y[j]) * h(sigma[t], x, c[t])) for t in xrange(len(c))] for j in
              xrange(len(y))]
    return result


def delta_sigma(x, y, y_, sigma, c, w, eta):
    return [-eta * sum((y_[j] - y[j]) * w[j][t] for j in xrange(len(y)))
            * h(sigma[t], x, c[t]) * sum((x[i] - c[t][i]) ** 2 for i in xrange(len(x))) * 1.0 / (sigma[t] ** 3)
            for t in xrange(len(sigma))]


def beta(sigma):
    return 1.0 / (2 * sigma * sigma)


def calculate(x, w, sigma, c):
    hs = [h(sigma[t], x, c[t]) for t in xrange(len(sigma))]
    y_s = [sum(w[j][t] * hs[t] for t in xrange(len(hs))) for j in xrange(len(w))]
    return y_s


def init_c(xs, q):
    return [xs[- i - 1 + (q >> 1)] for i in xrange(q)]


def stop(mat):
    _2d = type(mat[0]) == list or type(mat[0]) == tuple
    if _2d:
        for v in mat:
            for i in v:
                if abs(i) >= precision:
                    return False
    else:
        for i in mat:
            if abs(i) >= precision:
                return False

    return True


def train(xs, ys, eta_w, eta_c, eta_b, lmbda, q=10, c1=None, sigma1=None, w1=None, limit=10000):
    """
    以单隐层rbf神经网络拟合图线
    :param xs: xs样本集合
    :param ys: 实际标记值（非0,1,而是一个实值）
    :param q: q隐含层节点数
    :return:w, c, beta 分别为权重系数，中心坐标，方差
    """
    n = len(ys[0])  # 输出层的节点数
    m = len(xs[0])  # 输入层的节点数
    c = c1 if c1 is not None else init_c(xs, q)
    sigma = sigma1 if sigma1 is not None else [1.0 for i in xrange(q)]
    w = w1 if w1 is not None else [[0.0 for j in xrange(q)] for i in xrange(n)]
    print('c = {}, sigma = {}, w = {}'.format(c, sigma, w))
    time = 0
    while True:
        flag = True
        if time % 100 == 0:
            print('time = {}'.format(time))
            print('c = {}, sigma = {}, w = {}'.format(c, sigma, w))

        for i in xrange(len(xs)):
            y_ = calculate(xs[i], w, sigma, c)
            dc = delta_c(xs[i], ys[i], y_, w, sigma, c, eta_c)
            ds = delta_sigma(xs[i], ys[i], y_, sigma, c, w, eta_b)
            dw = delta_w(xs[i], ys[i], y_, sigma, c, lmbda, w, eta_w)
            new_c = matrix_add(c, dc)
            new_s = matrix_add(sigma, ds)
            new_w = matrix_add(w, dw)
            c = new_c
            sigma = new_s
            w = new_w
            flag = flag and stop(dc) and stop(ds) and stop(dw)

        if flag or time >= limit:
            return c, sigma, w
        time += 1


def test(txs, tys, c, w, sigma, mx=1, mi=0):
    p = re.compile('[\[\],]')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    y_s = [calculate(x, w, sigma, c)[0] for x in txs]
    ys = [f[0] for f in tys]
    print('均方误差: {}'.format(cal_error_of_mean_squre(ys, y_s)))
    y_s2 = [f * (mx - mi) + mi for f in y_s]
    ys2 = [f * (mx - mi) + mi for f in ys]
    print('均方误差2: {}'.format(cal_error_of_mean_squre(ys2, y_s2)))
    with open('test_result.dat', 'w') as f:
        for i in xrange(len(txs)):
            # print( 'before sub: {} {}'.format(txs[i], y_s[i]))
            # print( p.sub('', 'after sub: {} {}'.format(txs[i], y_s[i])))
            f.write(p.sub('', '{} {} {}\n'.format(txs[i], y_s[i], y_s2[i])))

    x1s = list()
    x0s = list()
    set(((x0s.append(x[0]), x1s.append(x[1])) for x in txs))
    ax.scatter(x0s, x1s, ys, c='b', marker='o')
    ax.scatter(x0s, x1s, y_s, c='r', marker='^')
    ax.set_xlabel('x0')
    ax.set_ylabel('x1')
    ax.set_zlabel('y')
    plt.show()
    return ax


def cal_error_of_mean_squre(ys, y_s):
    """
    计算均方误差
    :param ys:真实值
    :param y_s:预测值
    :return: 均方误差
    """
    if type(ys[0]) == list or type(ys[0]) == tuple:
        return sum([(ys[i][j] - y_s[i][j]) ** 2 for i in xrange(len(ys)) for j in xrange(len(ys[i]))]) / len(ys)
    else:
        return sum((ys[i] - y_s[i]) ** 2 for i in xrange(len(ys)))


def sigmoid_normalization(x):
    return 1.0 / (1 + exp(-x))


def main():
    choose_test_from_train = True
    p = re.compile(u'[\t ]+')
    xs = list()
    ys = list()
    txs = list()
    tys = list()
    with open('train.dat', 'r+') as f:
        for line in f:
            l = [float(s.replace('\n', '')) for s in p.split(line)]
            ys.append([l[-1]])
            del l[-1]
            xs.append(l)

    with open('test.dat', 'r+') as f:
        for line in f:
            l = [float(s.replace('\n', '')) for s in p.split(line)]
            tys.append([l[-1]])
            del l[-1]
            txs.append(l)

    print('xs = {}'.format(xs))
    print('ys = {}'.format(ys))
    print('txs = {}'.format(txs))
    print('tys = {}'.format(tys))

    c1, w1, sigma1 = None, None, None
    c, sigma, w = train(xs, ys, 0.1, 0.1, 0.1, 0.0001, 20, c1=c1, w1=w1, sigma1=sigma1, limit=5000)

    print("c = {}, sigma = {}, w = {}".format(c, sigma, w))
    ax = test(txs, tys, c, w, sigma, mx=1183, mi=28)


if __name__ == '__main__':
    main()
