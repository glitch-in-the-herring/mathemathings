n = int(input("Graph size: "))

matrix = []

for i in range(n):
    matrix.append([None] * n)

for i in range(n):
    for j in range(i, n):
        if j == i:
            matrix[i][j] = 0
            continue
        v = int(input(f"Vertex {i} to {j}: "))
        matrix[i][j] = v
        matrix[j][i] = v


a = int(input("Starting point: "))
v = [0] * n
d = 0
r = 0
minn = -1
minidx = a
w_0 = []
w_t = [-1] * n

def smallest(a, b):
    if a == -1:
        return b
    elif b == -1:
        return a
    if a < b: return a
    else: return b

w_t[a] = 0
v[a] = 1
d += 1

while d < n:
    w_0 = w_t.copy()
    minn = -1
    for i in range(n):
        if v[i]:
            continue
        if matrix[a][i] == -1:
            w_t[i] = -1
            continue
        w_t[i] = smallest(w_0[i], r + matrix[a][i])
        minn = smallest(minn, w_t[i])
        if minn == w_t[i]:
            minidx = i
    v[minidx] = 1
    a = minidx
    r = minn
    d += 1
    

