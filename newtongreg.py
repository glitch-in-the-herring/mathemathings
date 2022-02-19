def enc(p, c):
    c.append(p[0])
    b = []
    for i, j in zip(p[1:], p[:-1]):
        b.append(i - j)
        
    if len(p) > 1:
        return enc(b, c)
