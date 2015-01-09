t = input()

x = 0

for t in xrange(t):
    code = raw_input()
    if code == "++X":
        x += 1
    if code == "X++":
        x += 1
    if code == "X--":
        x -= 1
    if code == "--X":
        x -= 1
print x
