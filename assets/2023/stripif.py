# Strip conditionals from LaTeX
# Usage: stdin = conditional .tex file, stdout = stripped
# Conditionals must be defined by \newif\ifX\Xtrue (or Xfalse)
# and used as \ifX ... \else ... \fi on separate lines without comments

import sys
conditionals = {}
truthstack = []
truth = {"false": False, "true": True}

def newif(line):
    """Look for newif and if parsed, handle it"""
    if not line.startswith("\\newif"):
        return False
    pieces = line.split("\\")
    if len(pieces) != 4 or pieces[0] != "" or pieces[1] != "newif":
        print("%Wrong number of pieces: "+line)
        return False
    if not pieces[2].startswith("if"):
        print("%Missing if: "+line)
        return False
    name = pieces[2][2:]
    if not pieces[3].startswith(name):
        print("%Name missing: "+line)
        return False
    value = pieces[3][len(name):]
    if not value in truth:
        print("Misunderstood truth value: "+line)
        return False
    conditionals["\\if"+name] = truth[value]
    return True

for line in sys.stdin:
    line = line.strip()
    if '%' in line:
        line = line.split('%')[0]
    if newif(line):
        continue
    elif line in conditionals:
        truthstack.append(conditionals[line])
    elif line == "\\else":
        truthstack[-1] = not truthstack[-1]
    elif line == "\\fi":
        truthstack.pop()
    elif (not truthstack) or truthstack[-1]:
        print(line)
