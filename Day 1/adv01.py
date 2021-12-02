def day1pt1():

	depths = [int(i) for i in open("input.txt", 'r').read().splitlines()]
def day1pt1():

	D = [int(i) for i in open('input.txt', 'r').read().splitlines()]
	return sum([D[i-1] < D[i] for i in range(1, len(D))])
	
def day1pt2():

	d = [int(i) for i in open('input.txt', 'r').read().splitlines()]
	D = [d[i] + d[i+1] + d[i+2] for i in range(len(d) - 2)]
	return sum([D[i-1] < D[i] for i in range(1, len(D))])

print(day1pt1())
print(day1pt2())