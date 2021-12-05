def day2pt1(course):

	depth, x = 0, 0

	for c in course:
		if c[0] == 'forward':
			x += int(c[1])
		else:
			if c[0] == 'down':
				depth += int(c[1])
			else:
				depth -= int(c[1])

	return depth * x


def day2pt2(course):

	aim, depth, x = 0, 0, 0

	for c in course:
		if c[0] == 'forward':
			x += int(c[1])
			depth += aim * int(c[1])
		else:
			if c[0] == 'down':
				aim += int(c[1])
			else:
				aim -= int(c[1])

	return depth * x


with open('input.txt', 'r') as f:
		course = [i.split() for i in f.read().splitlines()]

print(day2pt1(course))
print(day2pt2(course))