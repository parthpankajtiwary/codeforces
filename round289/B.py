
n, k = map(int, raw_input().split())

a = [int(x) for x in raw_input().split()]

if max(a) - min(a) > k:
	print "NO"
else:
	print "YES"

	for x in a:
		array = ["#" for y in xrange(x)]
		color = 1
		for y in xrange(len(array)):
			if color%k == 0:
				array[y] = str(k)
			else:
				array[y] = str(color%k)
			color += 1			
		print " ".join(array)	