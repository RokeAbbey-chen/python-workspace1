# -*- coding:utf-8 -*-
import re
import pprint as pp
import math

'''以打地鼠为例，分数档位分为10档，从0-199 200-399 400-599，，，，1800-2000（多一分）,均为闭区间, 传入的特征就是这十档的次数'''


def dist(x, u):
    """
    :param x: 样本向量
    :param u: 中心点u坐标向量
    :return: x - u 的二阶范数平方
    """
    # print u'x : {},\n u : {}'.format(x, u)
    return sum(((x[i] - u[i]) ** 2) for i in xrange(0, len(x)))


def min_dist_index(x, us):
    u = min((u for u in us), key=lambda u: dist(x, u))
    return us.index(u)


def new_us(cluster):
    us = list()
    for c in cluster:
        le = len(c)
        if le <= 0:
            continue
        us.append(list(sum(x1) / le for x1 in zip(*c)))
    return us


def train(train_data, nu):
    """
    :param train_data: 训练数据
    :param nu: 中心向量个数
    :return: 最终定型的中心向量
    """
    le = len(train_data)
    if nu >= le:
        raise BaseException(u'样本数量必须大于中心点数目 样本数量为: {:2d}, 中心点个数为{}'.format(le, nu))

    """
    选定前nu个向量作为初始中心向量
    """
    us = list((train_data[i] for i in xrange(0, nu)))
    """
    为每个类设置一个集合用于容纳该类别的成员
    """
    cluster = tuple((list([u]) for u in us))
    """
    为每个成员记录各自所属的类，-1代表还未分类， 其余记录的是类下标
    """
    indexes = list((-1 for i in xrange(0, le)))
    indexes[0:nu] = xrange(0, nu)

    quit_flag = False
    limit = 1000
    times = 0
    while times <= limit and not quit_flag:
        i = 0
        for sp in train_data:
            # print sp
            min_index = min_dist_index(sp, us)
            if indexes[i] != -1:
                cluster[indexes[i]].remove(sp)
            indexes[i] = min_index
            cluster[min_index].append(sp)
            i += 1

        newus = new_us(cluster)
        quit_flag = newus == us
        us = newus
        print 'times : {}'.format(times)
        times += 1

    print u'前十个样本所属的类别'
    for i in xrange(0, min(len(indexes), 10)):
        print '第{:d}个样本的类别为{:d}'.format(i, indexes[i])
    print ''
    print u'第十类样本值:'
    for i in xrange(0, len(indexes)):
        if indexes[i] == 9:
            print u'第{}个样本，值:{}, 是否在cluster中 : {}'.format(i, train_data[i], train_data[i] in cluster[9])
    print ''

    print '各类人数：{}'.format([len(c) for c in cluster])

    print '各类别标准差: {}'.format(
        pp.pformat(
            tuple([round(
                math.sqrt(sum([(cluster[i][j][k] - us[i][k]) ** 2 for j in xrange(len(cluster[i]))]) / len(cluster[i])),
                2) for k in xrange(len(us[i]))] for i in xrange(len(cluster)))
        )
    )
    print '各样本距离中心点的平均距离: {}'.format(
        pp.pformat(
            tuple(
                round(
                    sum(
                        math.sqrt(dist(cluster[i][j], us[i])) / float(len(cluster[i]))
                        for j in xrange(len(cluster[i]))
                    ), 2) for i in xrange(len(cluster)))
        )
    )
    return us


def main():
    train_file = u'./test1.dat'
    normalization = True
    p = re.compile(u'[\t ]+')
    train_data = list()
    nu = 10
    with open(train_file, 'r+') as f:
        for line in f:
            l = [int(i.replace('\n', '')) for i in p.split(line)]
            l[0] = 0
            s = sum(l)
            if normalization:
                l = map(lambda x: int(x * 100.0 / s), l)
            train_data.append(l)

    us = train(train_data, nu)
    print '结果:'
    for u in us:
        print '{}'.format(u)


if __name__ == u'__main__':
    main()
