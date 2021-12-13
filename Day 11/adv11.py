def day11pt1(takos):
	pass


def day11pt2(takos):
	pass


with open('easyinput.txt', 'r') as f:
	f = f.read().splitlines()
	takos = [[int(i) for i in j.split()] for j in f]

print(day11pt1(takos))
print(day11pt2(takos))