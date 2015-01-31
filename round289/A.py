

n = input()

array = [["#" for x in xrange(n)] for y in xrange(n)]

for y in xrange(n):
	array[0][y] = 1


for x in xrange(1, n):
	for y in xrange(n):
		if y != 0:
			array[x][y] = array[x-1][y] + array[x][y-1]
		if y == 0:
			array[x][y] = array[x-1][y]
print array
print array[n-1][n-1]					