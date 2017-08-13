import sys
expansions = {
    "0": sys.argv[-4],
    "1": sys.argv[-3]
}
iters = int(sys.argv[-2])

word = sys.argv[-1]
for i in range(iters):
    word = "".join(expansions[x] for x in word)

print word
