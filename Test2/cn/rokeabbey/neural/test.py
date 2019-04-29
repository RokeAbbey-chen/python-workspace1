# import gaussian_rbf as gr
#
# sigma = [0.1 * i for i in xrange(1, 10)]
# w = [[0.07 * i * i for i in xrange(1, 10)]]
# c = [[0.1 * i * i * i, 0.2 * (i - 0.5) * i] for i in xrange(1, 10)]
#
# print [gr.gaussian_func(0.11, [0.3, 0.7], [0.37, 0.17])]
# print [gr.calculate([0.3, 0.7], w, sigma, c)]
# print 's1= {}; w1 = {}; c1 = {};'.format(sigma, w, c)