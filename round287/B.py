from math import sqrt, ceil

r, x, y, x1, y1 = map(int, raw_input().split())

distance = sqrt((x-x1)**2 + (y-y1)**2)
print distance
steps = 0
if distance <= 2*r:
	steps = 1
if distance == 0.0:
	steps = 0
if distance > 2*r:
	stepCount = distance-distance%(2*r)
	remaining = distance%(2*r)
	steps += stepCount/(2*r)
	print stepCount
	print remaining
	if remaining != 0.0:
		steps += 1

print int(steps)			
