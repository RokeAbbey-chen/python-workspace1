# -*- coding:utf-8 -*-
"""
    专门生成用于训练和测试logistic的数据
"""
import random as rd
import pprint as pp


def generate(w, ratio, n, c):
    """
    用于生成logistic训练和测试数据的集
    :param w: 目标权重系数, 注意w中包含常数项b, 且为了简便，w中的元素不得为0，为0的话就会出现平行于某一维度这种情况，不能生成数据
    :param ratio: 标记错误率, 填写整数, 代表生成的数据中有百分之ratio是噪音，100则为生成的数据全是噪音，0则代表生成的数据没有噪音
    :param n: 生成数据集的大小
    :param c: 正例的比例 c%, c为整数
    :return: 生成的数据集及其标记
    """
    c *= n / 100
    ratio *= n / 100
    xs = list()
    ys = list()
    for i in xrange(n):
        le = len(w)
        x = list()
        '注意le - 2是因为生成的数据集x最后一个维度固定为1, 并且倒数第二个维度用来调控是否改数据集所处的位置(默认w各项元素不为0)'
        for j in xrange(le - 2):
            x.append(rd.randint(0, 100))
        x[le - 2: le] = (0, 1)  # 此处第一项赋值为0是为了后面求和的时候直接忽视该项， 最后项赋值为1则对应w的常数项b
        limit = - sum(x[j] * w[j] for j in xrange(len(w))) / w[-2]    # 新生成的x[-2]的临界值
        if i < c:
            x_down_limit = limit
            x[-2] = x_down_limit + rd.randint(1, 10)
            ys.append(1)
        else:
            x_up_limit = limit
            x[-2] = x_up_limit - rd.randint(1, 10)
            ys.append(0)
        del x[-1]
        xs.append(x)

    wrong_index = set()
    while len(wrong_index) < ratio:
        wrong_index.add(rd.randint(0, n - 1))

    '在原本正确分类的样本中制造ratio个噪音'
    for i in wrong_index:
        ys[i] = int(not ys[i])

    return xs, ys


def main():
    w = [1, 2, 0]
    xs, ys = generate(w, 0, 2000, 50)
    for i in xrange(len(xs)):
        xs[i].append(ys[i])

    print "样本 : \n{}".format(pp.pformat(xs))
    xs_t = zip(*xs)
    for s in xs_t:
        print s


if __name__ == '__main__':
    main()












