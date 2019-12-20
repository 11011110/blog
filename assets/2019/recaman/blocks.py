def cubes():
    i = 1
    while True:
        yield i*i*i
        i += 1

visited = set()
a = n = 0
x = 0
y = 1
b = 0
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
    if a not in visited:
        visited.add(a)
        neighbors = 0
        if a-1 in visited:
            neighbors += 1
        if a+1 in visited:
            neighbors += 1
        b += 1 - neighbors
    if n == target:
        print("%d\t%f" % (n,(x*1.0)/b))
        target = targets.next()
