
def sumOfDigits(n, number):
	array = [int(x) for x in n]
	sum = 0
	for x in array:
		sum += x
	return sum == number

t = input()
b = []
for x in xrange(t):
	b.append(input())

minimum = 0
while(not sumOfDigits(str(minimum), b[0])):
	minimum += 1
	
a = [minimum]
for x in xrange(1, len(b)):
	y = a[-1] + 1
	while(not sumOfDigits(str(y), b[x])):
		y += 1
	a.append(y)

for x in a:
	print x	
