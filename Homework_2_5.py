a = [[1,2,3],[4,5,6]]
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m = len(a)                                             # a: m × n
n = len(b)                                             # b: n × k
k = len(b[0])

c = [[None for __ in range(k)] for __ in range(m)]     # c: m × k

for i in range(m):
    for j in range(k):
        c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))

print(c)