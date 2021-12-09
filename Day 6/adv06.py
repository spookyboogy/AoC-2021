from math import floor
from time import time
import datetime


def day6pt1(fish):
	""" Relatively fast but extremely memory-inefficient"""

	def propagate(fishes, days):
		
		if days == 0:
			return fishes
		else:
			births = fishes.count(0)
			fishes = [i-1 if i!= 0 else 6 for i in fishes]
			return fishes + propagate([9] * births, days - 1)

	day, end = 0, 80
	while day < end:
		fish = propagate(fish, end - day)
		day += 1
	return len(fish)


def day6pt2(fishes):
	""" Simple iterative version, less efficient than pt1 recursion """

	day, end = 0, 80
	while day < end:
		for i in range(len(fishes)):
			if fishes[i] == 0:
				fishes += [8]
				fishes[i] = 6
			else:
				fishes[i] -= 1
		day += 1
	return len(fishes)


def day6pt3(fishes):
	"""math way per fish, faster but still too slow"""
	
	def propagate(fish, days):

		if days == 0:
			return 1
		else:
			bdays = (i-1 for i in range(days - fish, 0, -7))
			return 1 + sum(propagate(8, bday) for bday in bdays)

	end_day = 80
	return sum(propagate(i, end_day) for i in fishes)


def day6pt4(fishes):
	"""
	Math+recursion way per fish, fastest yet. still slow and inefficient,
	but will run forever w/o MemoryError
	"""
	
	def spawncount(fish, days):
		if days == 0:
			return 1
		else:
			#births = floor(days/7) + int(f <= days%7)
			bdays = (i-1 for i in range(days - fish, 0, -7))
			return 1 + sum(spawncount(8, bday) for bday in bdays)

	fishes = (i for i in fishes)
	school, end = 0, 80
	for f in fishes:
		school += spawncount(f, end)
	return school


def day6pt5(fishes):
	""" Use a recurrence relation """
	pass


with open('input.txt', 'r') as f:
	f = f.read().splitlines()[0]
	fish = [int(i) for i in f.split(',')]

print('pt 1 = {}'.format(day6pt1(fish)))
print('working...')
t0 = time()
print(day6pt4(fish))
t1 = time()
endtimes = datetime.timedelta(seconds=t1-t0)
print('time to complete: {}'.format(endtimes))