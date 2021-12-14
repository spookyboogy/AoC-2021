import os, time
try:
	import colorama as cr
	cr.init(autoreset=True)
	colorful = True
except:
	colorful = False


def day11pt1(takos, steps=100, verbose=True, refresh=True):
	"""So much tako fun"""

	def print_takos(takos, step, flashed=None, 
					width=1, pause=.5, refresh=True):
		
		if not verbose: return	
		def cls():
			os.system('cls' if os.name=='nt' else 'clear')
		
		print('\ntakos {}:'.format(step))
		for j in range(len(takos)):
			for i in range(len(takos[j])):
				tako = takos[j][i]
				if colorful and flashed and (j, i) in flashed:
					print(cr.Fore.GREEN + 
						'{0:{width}}'.format(tako,width=width), end='')
				else:
					print('{0:{width}}'.format(tako,width=width), end='')
			print()
		if refresh:
			time.sleep(pause)
			if step != steps:
				cls()

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

	step, flashes, hnnnnng = 0, 0, 0
	print_takos(takos, step, refresh=refresh)
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
		print_takos(takos, step, flashed, refresh=refresh)
		if len(flashed) == len(takos) * len(takos[0]):
			hnnnnng = step
			break
	return [flashes, hnnnnng]


def day11pt2(takos):
	
	max_steps = ((len(takos) * len(takos[0])) ** 2) // 10
	return day11pt1(takos, steps=max_steps, verbose=False)[1]


with open('easyinput.txt', 'r') as f:
	f = f.read().splitlines()
	takos = [[int(i) for i in j] for j in f]
	tako_copy = [[int(i) for i in j] for j in f]

print(day11pt1(takos)[0])
print(day11pt2(tako_copy))