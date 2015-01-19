

graph = {}

n, m = map(int, raw_input().split())

for x in xrange(m):
	a, b, c = map(int, raw_input().split())
	if (a, b) not in graph:
		graph[(a, b)] = [c]
		graph[(b, a)] = [c]
	if (a, b) in graph:
		if c not in graph[(a, b)]:
			graph[(a,b)].append(c)
	if (b, a) in graph:
		if c not in graph[(b, a)]:
			graph[(b, a)].append(c)								

q = input()
answers = []
for x in xrange(q):
	u, v = map(int, raw_input().split())
	
	if (u, v) in graph:
		answers.append(len(graph[(u, v)]))
	if (v, u) in graph:
		answers.append(len(graph[(v, u)]))	
	else:
		points = []
		for x in xrange(u, v):
			points.append((x, x+1))	
		print points		
		colors = 0
		for color in graph[points[0]]:
			for x in points:
				if color not in graph[x]:
					flag = False
			if flag:
				colors += 1		
		answers.append(colors)
print answers				
				



			

	 
