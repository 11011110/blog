# Brute force search to check reverse search antimatroid generator

def full(x):
    return x & (1<<15) != 0
    
def bits(x):
    while x:
        b = x &~ (x-1)
        yield b
        x &=~ b

predecessors = {}
for i in range(16):
    predecessors[1<<i] = sum([1<<(i&~b) for b in bits(i)])

def accessible(x):
    for b in bits(x):
        if b != 1 and predecessors[b] & x == 0:
            return False
    return True

def unionclosed(x):
    for i in range(16):
        for j in range(16):
            if x & (1<<i) and x & (1<<j) and not (x & (1<<(i|j))):
                return False
    return True

for x in range(1<<16):
    if full(x) and accessible(x) and unionclosed(x):
        print x
