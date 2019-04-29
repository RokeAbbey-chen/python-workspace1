class Matrix(object):

    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.mat = [[0 for j in xrange(d2)] for i in xrange(d1)]



