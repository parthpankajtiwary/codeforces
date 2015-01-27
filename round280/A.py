

n = input()
sum = 0
x = 0
while(sum < n):
	if(sum >= n):
		print x
	else:	
		x += 1
		sum += (x*(x+1))/2
		print sum

