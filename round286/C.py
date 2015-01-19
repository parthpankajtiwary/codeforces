

visited = []

n, d = map(int, raw_input().split())
location = []
for x in xrange(n):
	location.append(input())

def dfs(state):
	if state not in visited:
		
		visited.append(state)
		if state in location:
			location.append('True')
			location.remove(state)
			return True
		l = state - visited.pop()	
		nextStateOne = state + 1
		nextStateTwo = state + l - 1  
		nextStateThree = state + l + 1
		dfs(nextStateOne)
		dfs(nextStateTwo)
		dfs(nextStateThree)

dfs(d)
print visited.count('True')			


