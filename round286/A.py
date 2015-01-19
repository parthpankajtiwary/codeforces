
def checkPalindrome(string):
	if len(string)%2 == 0:
		left = string[:len(string)/2]
		right = string[len(string)/2:][::-1]
		if right == left:
			return True
	if len(string)%2 != 0:
		left = string[:len(string)/2]
		right = string[len(string)/2+1:][::-1]
		if right == left:
			return True
	return False			

s = raw_input()

sArray = [x for x in s]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in xrange(len(sArray)+1):
	for y in alphabet:
		newString = sArray[:x] + [y] + sArray[x:]
		if checkPalindrome("".join(newString)):
			print "".join(newString)
			exit()
print "NA"		
