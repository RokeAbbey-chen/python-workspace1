# 前向算法
import numpy as np 
A = np.array([0.5, 0.2, 0.3, 0.3, 0.5, 0.2, 0.2, 0.3, 0.5])
A.shape = 3, -1
B = np.array([0.5, 0.5, 0.4, 0.6, 0.7, 0.3])
B.shape = 3, -1
pii = np.array([0.2, 0.4, 0.4])
T = 3
O = np.array([0, 1, 0]) #	红 白 红
alpha = [[], []]
alpha[0]= np.array([pii[i] * B[i][O[0]] for i in range(len(pii))])
for k in range(1, T):
	alpha[k & 1] = np.array([alpha[(k - 1) & 1] @ A[:, i].T * B[i][O[k]] for i in range(len(pii))])

print(alpha[(T - 1) & 1].sum())



