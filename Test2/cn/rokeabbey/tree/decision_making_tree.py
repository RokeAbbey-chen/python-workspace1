# -*- coding:utf-8 -*-
import numpy as np
import math
class DecisianMakingTree():

    def __init__(self, sxs=None, sys=None, txs=None, tys=None, discrete=None):
        """
        :param sxs: 训练样本特征
        :param sys: 训练样本标记, 样本标记请用连续的自然数
        :param txs: 测试样本特征
        :param tys: 测试样本标记, 样本标记请用连续的自然数
        :param discrete: boolean数组，True代表对应的属性是离散属性，False代表为连续属性
        """
        self.sxs = sxs
        self.sys = sys
        self.txs = txs
        self.tys = tys
        self.discrete = discrete
        self.name2num = []  # 映射各个离散属性名称与其标号的dict
        self.num2name = []  # 映射各个离散属性标号与其名称的dict
        self.lift_data(sxs, sys)
        self.lift_data(txs, tys)
        self.init_name_num_dict(self.sxs)

    @staticmethod
    def ent(ps):
        return -sum(ps * np.array([math.log(p) for p in ps]))

    def gain(self, xs, ys, field, w):
        """
        获取信息增益
        :param xs:当前子树的样本集
        :param ys:当前子树的标记集
        :param field:属性下标
        :return:
        """
        cnt = np.zeros(max(ys) + 1)
        total_cnt = len(ys)
        for y in ys:
            cnt[y] += 1
        ps = cnt / float(total_cnt)
        et = self.ent(ps)
        if self.discrete[field]:
            d = dict()
            for x in xs:
                d.setdefault(x[field], 0)
                d[x[field]] += 1

            sd = sum(d.values()) - d[self.name2num['-']]
            return et - sum([float(dv) / sd for dv in d.values()])
        else:
            continious_field = []
            for x in xs:
                if x[field] != '-':
                    continious_field.append(x[field])

            continious_field.append(min(continious_field))
            continious_field.append(max(continious_field))
            continious_field = sorted(continious_field)
            lcf = len(continious_field);
            mxk = 0
            mxv = 0
            for i in xrange(1, lcf):
                k = (continious_field[i] + continious_field[i - 1]) / 2.0






    def getBestPoint(self, xs, field):
        pass

    def fit(self):
        pass

    @staticmethod
    def lift_data(xs, ys=None):
        if xs is None:
            return
        if ys is None:
            ys = []
            for x in xs:
                ys.append(x[-1])
                del x[-1]

    def init_name_num_dict(self, xs):
        zxs = zip(xs)
        for zx in zxs:
            d = {}
            d2 = {}
            for i in zx:
                if i not in d:
                    d2[len(d)] = i
                    d[i] = len(d)

            self.name2num.append(d)
            self.num2name.append(d2)









