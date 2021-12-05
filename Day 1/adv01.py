def day1pt1(data):

	return sum([data[i-1] < data[i] for i in range(1, len(data))])

	
def day1pt2(data):

	D = [data[i] + data[i+1] + data[i+2] for i in range(len(data) - 2)]
	return sum([D[i-1] < D[i] for i in range(1, len(D))])


with open('input.txt', 'r') as f:
	report = [int(i) for i in f.read().splitlines()]

print(day1pt1(report))
print(day1pt2(report))