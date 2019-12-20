visited = set()
a = n = 0
high = 0
while n < 250000000:
    n += 1
    if a > n and a - n not in visited:
        a -= n
    else:
        a += n
    visited.add(a)
    if a > high:
        print("%d\t%f" % (n,a*1.0/n))
        high = a*1.005