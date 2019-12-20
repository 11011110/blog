def cubes():
    i = 1
    while True:
        yield i*i*i
        i += 1

visited = set()
a = n = 0
x = 0
y = 1
targets = cubes()
target = targets.next()
while n < 250000000:
    n += 1
    if a > n and a - n not in visited:
        a -= n
        if y < 0:
            x += 1
        else:
            y = -1
    else:
        a += n
        if y > 0:
            x += 1
        else:
            y = 1
    visited.add(a)
    if n == target:
        print("%d\t%d" % (n,x))
        target = targets.next()