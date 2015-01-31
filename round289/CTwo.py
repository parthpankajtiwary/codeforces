# def sumOfDigits(n, number):
# 	array = [int(x) for x in n]
# 	sum = 0
# 	for x in array:
# 		sum += x
# 	return sum == number

def findNextLess(number, difference):
	numberArray = [int(x) for x in number]
	numberArray.reverse()
	d = difference
	for x in xrange(len(numberArray)):
		if difference <= (9 - numberArray[x]):
			numberArray[x] += difference
			difference = 0
		elif difference > (9 - numberArray[x]):
			numberArray[x] += (9 - numberArray[x])
			difference -= (9 - numberArray[x])
	#if difference > 9:
	print difference	
	if difference <= 9:
		numberArray.append(difference)				
	return numberArray[::-1]			

print findNextLess("3999", 10)
# def findNextLess(number, difference):



# t = input()
# b = []
# for x in xrange(t):
# 	b.append(input())

# minimum = 0
# while(not sumOfDigits(str(minimum), b[0])):
# 	minimum += 1

# a = [minimum]
# for x in xrange(1, len(b)):
