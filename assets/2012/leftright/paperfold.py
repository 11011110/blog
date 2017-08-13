import sys
iters = int(sys.argv[-1])

word = "1",
for n in range(iters):
    next = ["1"]
    for i in range(len(word)):
        next.append(word[i])
        next.append(str(i&1))
    word = "".join(next)

print word
