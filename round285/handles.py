
t = input()

name = {}

def findKey(x):
    for y in name:
        if name[y] == x:
            return y

for x in xrange(t):
    old, new = map(str, raw_input().split())
    name[old] = new


for x in name.values():
    key = findKey(x)
    if x in name:
        name[key] = name[x]
        del name[x]
print len(name)
for x in name:
    print x + " " + name[x]
