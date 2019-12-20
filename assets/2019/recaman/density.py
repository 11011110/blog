def cubes():
    i = 1
    while True:
        yield i*i*i
        i += 1

visited = set()
a = n = 0
targets = cubes()
target = targets.next()
while n < 250000000:
    n += 1
    if a > n and a - n not in visited:
        a -= n
    else:
        a += n
    visited.add(a)
    if n == target:
        print("%d\t%d" % (n,a))
        target = targets.next()