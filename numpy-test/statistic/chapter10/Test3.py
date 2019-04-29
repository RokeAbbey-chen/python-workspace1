import numpy as np
A = np.array([0.5, 0.2, 0.3, 0.3, 0.5, 0.2, 0.2, 0.3, 0.5])
A.shape = 3, -1
B = np.array([0.5, 0.5, 0.4, 0.6, 0.7, 0.3])
B.shape = 3, -1
pii = np.array([0.2, 0.4, 0.4])
O = np.array([0, 1, 0])

dp = np.zeros((2, 3))
index = np.zeros((O.size, 3))

for i in range(3):
	dp[0][i] = pii[i] * B[i][O[i]]
	index[0][i] = -1;

for t in range(1, O.size):
	dp[t & 1] = [(dp[(t - 1) & 1] * A[:, i]).max() * B[i][O[t]] for i in range(O.size)]
	index[t] =  [(dp[(t - 1) & 1] * A[:, i]).argmax() for i in range(O.size)]
rIdx = dp[(O.size - 1) & 1].argmax()
I = np.zeros(O.size, dtype=np.int32)
I[I.size - 1] = rIdx 
for i in range(I.size - 2, -1, -1):
	I[i] = index[i + 1][I[i + 1]]

print (dp[(O.size - 1) & 1][rIdx], I)



