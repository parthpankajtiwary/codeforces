
a, b, c, d = map(int, raw_input().split())

mishaScore = max(3*a/10, a-a/250*c)
vasyaScore = max(3*b/10, b-b/250*d)

if mishaScore > vasyaScore:
    print "Misha"
if mishaScore < vasyaScore:
    print "Vasya"
if mishaScore == vasyaScore:
    print "Tie"
