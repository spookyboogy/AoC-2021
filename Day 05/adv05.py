def day5pt1(points):

	points = [i for i in points if i[0][0] == i[1][0] or i[0][1] == i[1][1]]
	max_x = max([max(i[0][0], i[1][0]) for i in points])
	max_y = max([max(i[0][1], i[1][1]) for i in points])
	M = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]
	
	for p in points:	
		x0, x1, y0, y1 = p[0][0], p[1][0], p[0][1], p[1][1] 
		if x0 == x1:
			for i in range(min(y0,y1), max(y0,y1) + 1):
				M[i][x0] += 1
		else: 
			for i in range(min(x0,x1), max(x0,x1) + 1):
				M[y0][i] += 1

	return [sum([len([i for i in j if i > 1]) for j in M]), M]
	

def day5pt2(points):

	M = day5pt1(points)[1]
	points = [i for i in points if i[0][0]!=i[1][0] and i[0][1]!=i[1][1]]

	for p in points:

		if p[0][0] > p[1][0]:
			p = [p[1], p[0]]
		x0, x1, y0, y1 = p[0][0], p[1][0], p[0][1], p[1][1]

		if y0 < y1:
			for i in range(x1 - x0 + 1):
				M[y0 + i][x0 + i] += 1
		else: 
			for i in range(x1 - x0 + 1):
				M[y0 - i][x0 + i] += 1
				
	return sum([len([i for i in j if i > 1]) for j in M])


with open('input.txt', 'r') as f:
		f = [i.split('->') for i in f.read().splitlines()]
		points = [[tuple(int(i) for i in p.split(',')) for p in pts] for pts in f]

print('Part 1 answer = {}'.format(day5pt1(points)[0]))
print('Part 2 answer = {}'.format(day5pt2(points)))