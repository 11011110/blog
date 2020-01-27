def breadth_first(tree,children=iter):
    """Traverse the nodes of a tree in breadth-first order.
    The first argument should be the tree root; children
    should be a function taking as argument a tree node and
    returning an iterator of the node's children.
    """
    yield tree
    last = tree
    for node in breadth_first(tree,children):
        for child in children(node):
            yield child
            last = child
        if last == node:
            return

def gridLowerSubsets(a,b,c):
    if a*b*c==0:
        return iter([0])

    # node = bitmask where bit bcx+cy+z corresponds to position (x,y,z)
    # parent of node = remove LEAST significant bit from node
    # root = zero bitmask
    # children of node = add bits less sigificant than existing LSB
    always_ready_x = always_ready_y = always_ready_z = 0
    for x in range(a):
        for y in range(b):
            always_ready_z |= 1L<<(x*b*c+y*c+(c-1))
    for x in range(a):
        for z in range(c):
            always_ready_y |= 1L<<(x*b*c+(b-1)*c+z)
    for y in range(b):
        for z in range(c):
            always_ready_x |= 1L<<((a-1)*b*c+y*c+z)
    def children(q):
        less_sig = (q - 1) &~ q
        ready_x = (q >> (b*c)) | always_ready_x
        ready_y = (q >> c) | always_ready_y
        ready_z = (q >> 1) | always_ready_z
        addable = ready_x & ready_y & ready_z & less_sig
        while addable:
            bit = addable &~ (addable - 1)
            yield q | bit
            addable &=~ bit
    return breadth_first(0,children)

def ilen(g):
    i = 0
    for x in g:
        i += 1
    return i

def formula(a,b,c):
    numerator = 1
    denominator = 1
    for x in range(a):
        for y in range(b):
            for z in range(c):
                numerator *= (x+y+z+2)
                denominator *= (x+y+z+1)
    return numerator/denominator

for tot in range(11):
    for c in range(tot+1):
        for b in range(tot-c+1):
            print "%4d" % ilen(gridLowerSubsets(tot-b-c,b,c)),
#            print "%4d" % formula(tot-b-c,b,c),
        print
    print
