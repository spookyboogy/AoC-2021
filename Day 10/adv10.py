def day10pt1(subsys):
	
	pairs = [('()'), ('[]'), ('{}'), ('<>')]
	score_table = {')':3, ']':57, '}':1197, '>':25137}
	scores, pt2_lines = [], []
	for l in range(len(subsys)): 
		line = subsys[l]
		i = 0
		while i < len(line):
			for p in pairs:
				if p in line:
					line = line.replace(p,'')
			i += 1
		incomplete = True
		for c in range(len(line)):
			if line[c] in score_table.keys():
				scores += [score_table[line[c]]]
				incomplete = False
				break
		if incomplete:
			pt2_lines += [line]
	return [sum(scores), pt2_lines]


def day10pt2(incompletes):

	pairs = {'(':')', '[':']', '{':'}', '<':'>'}
	score_table = {')': 1, ']': 2, '}': 3, '>': 4}
	complete = [''.join(pairs[c] for c in line[::-1]) for line in incompletes]
	scores = []
	for line in complete:
		score = 0
		for c in line:
			score *= 5
			score += score_table[c]
		scores += [score]
	return sorted(scores)[len(scores)//2]


with open('input.txt', 'r') as f:
	subsystem = f.read().splitlines()	

pt1pt2 = day10pt1(subsystem)
print(pt1pt2[0])
print(day10pt2(pt1pt2[1]))