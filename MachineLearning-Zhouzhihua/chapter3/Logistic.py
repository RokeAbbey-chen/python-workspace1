# -*- coding:utf-8 -*-

import math

precision = 0.0001
w = [1, 1, 1, 1]
X = [
		[0.697, 0.46, 1, 1], 
		[0.774, 0.376, 1, 1],
		[0.634, 0.264, 1, 1],
		[0.608, 0.318, 1, 1],
		[0.556, 0.215, 1, 1],
		[0.403, 0.237, 1, 1],
		[0.481, 0.149, 1, 1],
		[0.437, 0.211, 1, 1],

		[0.666, 0.091, 1, 0],
		[0.243, 0.267, 1, 0],
		[0.245, 0.057, 1, 0],
		[0.343, 0.099, 1, 0],
		[0.639, 0.161, 1, 0],
		[0.657, 0.198, 1, 0],
		[0.36, 0.37, 1, 0],
		[0.593, 0.042, 1, 0],
		[0.719, 0.103, 1, 0]

	]

def trans(X):

	lr = len(X)
	lc = len(X[0])
	newX = list() 
	for i in xrange(0, lc):
		arr = []
		for j in xrange(0, lr):
			arr.append(X[j][i])

		newX.append(arr)
	return newX

X = trans(X)

def newton_method(w, X):

	l = len(X)	
	l2 = len(X[0])
	rg = xrange(0, l - 1)
	y = X[l - 1]
	w = list(w)
	newW = list(w)

	while True:
		flag = True
		for j in rg:
			numerator = sum(((y[i] - 1) * X[j][i] - X[j][i] / (math.exp(-w[j] * X[j][i]) + 1) for i in rg)) 
			denominator = sum((X[j][i] / ((math.exp(-w[j] * X[j][i]) + 1)) ** 2))
			newW[j] = w[j] + numerator / denominator
			flag = not (flag and abs(numerator ) > precision)
		t = w
		w = newW
		newW = t
		print u"最新的w : " + unicode(newW)
		if flag : return newW







for i in xrange(0, 10):
	print """t{}:{{ 
				$cond : {{ 
					if : {{$gte:['$integral', {}],  $lte:['$integral',{}]}} 
				}}
		}}""".format(i + 1, i * 200 , (i + 1) * 200 - 1)


		t1: {
				$cond : {if : {$lte:['$integral', 199]}}
			}




			



def logistic(w, X):

	pass
	
