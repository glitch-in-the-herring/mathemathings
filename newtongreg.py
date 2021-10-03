def enc(p, c):
    c.append(p[0])
    b = []
    for i in range(1, len(p)):
        b.append(p[i] - p[i-1])
        
    if len(p) > 1:
        return enc(b, c)
