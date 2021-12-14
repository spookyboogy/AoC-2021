import colorama as cr
cr.init(autoreset=True)


def day11pt1(takos, verbose=True):
	"""So much tako fun"""

	def print_takos(takos, step, flashed=None, width=1):
		
		if not verbose: return
		print('\ntakos {}:'.format(step))
		for j in range(len(takos)):
			for i in range(len(takos[j])):
				tako = takos[j][i]
				if flashed and (j, i) in flashed:
					#print('\033[;1m'+'{0:<1}'.format(tako), end = '')
					#spent 5 hrs trying to figure out how to get ANSI to work
					print(cr.Fore.GREEN + 
						'{0:{width}}'.format(tako,width=width), end = '')
				else:
					print('{0:{width}}'.format(tako,width=width), end = '')
			print()
	
	def flash(tako, flashed):
		
		y, x = tako[0], tako[1]
		takos[y][x] = 0
		neighbors = [(y-1,x-1), (y-1,x), (y-1,x+1),
					 (y  ,x-1), (y  ,x), (  y,x+1),
					 (y+1,x-1), (y+1,x), (y+1,x+1)]
		for nbor in neighbors:
			if -1 in nbor:
				continue
			try:
				if nbor in flashed:
					continue
				if takos[nbor[0]][nbor[1]] >= 9:
					flashed += [nbor]
					flashed = flash(nbor, flashed)
				else:
					takos[nbor[0]][nbor[1]] += 1
			except IndexError:
				continue
		return flashed

	flashes = 0
	hnnnnng = 0
	step, steps = 0, 100
	print_takos(takos, step)
	while step < steps:
		flashed = []
		for j in range(len(takos)):
			for i in range(len(takos[j])):
				takos[j][i] += 1
				if takos[j][i] > 9:
					tako = (j, i) 
					flashed += [tako]
					flashed = flash(tako, flashed)
		for tako in flashed:
			takos[tako[0]][tako[1]] = 0
		step += 1
		flashes += len(flashed)
		print_takos(takos, step, flashed)
		if len(flashed) == len(takos) * len(takos[0]):
			hnnnng = step
			break
	return [flashes, hnnnnng]


def day11pt2(takos):
	
	return day11pt1(takos,verbose=False)[1]


with open('easyinput.txt', 'r') as f:
	f = f.read().splitlines()
	takos = [[int(i) for i in j] for j in f]

print(day11pt1(takos)[0])
print(day11pt2(takos))