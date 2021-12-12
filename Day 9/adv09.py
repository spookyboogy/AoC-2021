def day9pt1(mapa):
	""" Surely, there's a more clever way than this. """

	jlen, ilen = len(mapa), len(mapa[0])
	lows = []
	for j in range(1, jlen-1): # inner
		for i in range(1, ilen-1):
			u, d = mapa[j-1][i], mapa[j+1][i]
			l, r = mapa[j][i-1], mapa[j][i+1]
			if mapa[j][i] < min(u, d, l, r):
				lows += [(j, i)]
	for i in range(1, ilen-1): # upper
		d = mapa[1][i]
		l, r = mapa[0][i-1], mapa[0][i+1]
		if mapa[0][i] < min(d, l, r):
			lows += [(0, i)]
	for j in range(1, jlen-1): # left
		r = mapa[j][1]
		u, d = mapa[j-1][0], mapa[j+1][0]
		if mapa[j][0] < min(r, u, d):
			lows += [(j, 0)]
	for j in range(1, jlen-1): # right
		l = mapa[j][-2]
		u, d = mapa[j-1][-1], mapa[j+1][-1]
		if mapa[j][-1] < min(l, u, d):
			lows += [(j, ilen - 1)]
	for i in range(1, ilen-1): # lower
		u = mapa[-2][i]
		l, r = mapa[-1][i-1], mapa[-1][i+1]
		if mapa[-1][i] < min(u, l, r):
			lows += [(jlen - 1, i)]

	if mapa[0][0] < min(mapa[0][1], mapa[1][0]): #corners
		lows += [(0,0)]
	if mapa[-1][-1] < min(mapa[-1][-2], mapa[-2][-1]):
		lows += [(jlen - 1, ilen - 1)]
	if mapa[0][-1] < min(mapa[0][-2], mapa[1][-1]):
		lows += [(0, ilen - 1)]
	if mapa[-1][0] < min(mapa[-1][1], mapa[-2][0]):
		lows += [(jlen - 1, 0)]

	return [sum(mapa[i[0]][i[1]] + 1 for i in lows), lows]


def day9pt2(mapa):
	
	def neighbor_check(p, basin):
		directions = [[-1,0], [1,0], [0,-1], [0,1]]
		val = mapa[p[0]][p[1]]
		for d in directions:
			try:
				nbor = (p[0]+d[0], p[1]+d[1])
				if nbor in basin or nbor[0] < 0 or nbor[1] < 0:
					continue
				nbor_val = mapa[nbor[0]][nbor[1]]
				if nbor_val > val and nbor_val != 9:
					basin += [nbor]
					basin += neighbor_check(nbor, basin)
			except IndexError:
				continue
		return [i for i in set(basin)]

	lows = day9pt1(mapa)[1]
	basin_lens = []
	for low in lows:
		basin_lens += [len(neighbor_check(low, [low]))]
	basin_lens = sorted(basin_lens)[-3:]
	return basin_lens[0] * basin_lens[1] * basin_lens[2]

	
with open('input.txt', 'r') as f:
	f = f.read().splitlines()
	mapa = [[int(i) for i in j] for j in f]

print(day9pt1(mapa)[0])
print(day9pt2(mapa))