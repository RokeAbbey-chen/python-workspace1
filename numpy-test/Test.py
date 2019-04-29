import numpy as np 
a = np.fromfunction(lambda x, y, z: 100 * x + 10 * y + z, (3, 4, 5), dtype=int)
# print(a)
# print(a[1:3, 1:3, 2:4])

a = np.arange(10)
a.shape = 2, 5
l1 = [[0, 1], [1, 0]]
l2 = [[3, 4], [1, 4]]
l = l1, l2
# l = np.array(l)
# print(a[l])


a = np.arange(9)
a.shape = 3, -1
lmd, v = np.linalg.eig(a)
# print(np.diag(lmd))
# print(v)
# print(v @ np.diag(lmd) @ np.linalg.inv(v))

a = np.array([[1, -1, 1], [2, -2, 2], [-1, 1, -1]])
lmd, P = np.linalg.eig(a)
print(np.diag(lmd))
print(P)
print(np.linalg.inv(P))
print(P @ np.diag(lmd) @ np.linalg.inv(P))



