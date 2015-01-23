n, k = map(int, raw_input().split())

a = [int(x) for x in raw_input().split()]
s = [int(x) for x in a]

a.sort()
indices = []
count = 0
sum = 0
indexRemoved = 0
for x in a:
	if sum <= k and (sum + x) <= k:
		sum += x
		count += 1
		if s.index(x) not in indices:
			indices.append(s.index(x))
			s = s[:s.index(x)] + ["#"] + s[s.index(x)+1:]
			print s				

print count
for x in indices:
	print x+1,