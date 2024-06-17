# file: util.py

def move(d, v, m):
    d = d + v
    if d < 0:
        d = 0
        v = -v
    elif d > m:
        d = m
        v = -v
    return d, v
