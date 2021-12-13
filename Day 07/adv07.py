from math import floor, factorial as fact


def day7pt1(crabs):
	
	pivot = crabs[floor(len(crabs) / 2)]
	return sum(abs(crab - pivot) for crab in crabs)
	 

def day7pt2(crabs):

	triangle = lambda n: (n**2 + n) // 2

	crabset = list(set(crabs))
	pivot0 = crabset[len(crabset)//2]
	pivot_n = crabset[len(crabset)//2 + 1]
	pivots = (i for i in range(pivot0, pivot_n + 1))
	costs = (sum(triangle(abs(i - pivot)) for i in crabs) for pivot in pivots)
	
	return min(costs)


with open('input.txt', 'r') as f:
	crabs = sorted(int(i) for i in f.read().split(','))
	
print(day7pt1(crabs))
print(day7pt2(crabs))