from itertools import combinations

def day4pt1(seq, boards):
	"""
	If you type and pronounce board enough times you being to question its spelling.
	"""
	
	n = 5
	while n < len(seq):	
		for board in boards: 
			marked = [i for i in seq[:n] if i in board[0]]		
			if len(marked) > 4:
				bingo = [set(i) for i in combinations(marked, 5)]
				for i in board[1]:
					if i in bingo:
						unmarked = [i for i in board[0] if i not in marked]
						return sum(unmarked) * seq[n-1]
		n += 1


def day4pt2(seq, boards):
	
	n = 5
	while n < len(seq) and len(boards) > 1:	
		for board in boards: 
			marked = [i for i in seq[:n] if i in board[0]]		
			if len(marked) > 4:
				bingo = [set(i) for i in combinations(marked, 5)]
				for i in board[1]:
					if i in bingo:
						boards.remove(board)
						break		
		n += 1

	unmarked = [i for i in boards[0][0] if i not in seq[:n]]
	return sum(unmarked) * seq[n-1]


with open('input.txt' , 'r') as f:
	f = f.read().split('\n\n')
	# Get Bingo number sequence
	seq = [int(i) for i in f[0].split(',')]
	# Get messy set of string boards
	boards = [i.split('\n\n') for i in f[1:]]
	# Turn boards into 1d lists of numbers
	boards = [[int(i) for i in b[0].replace('\n',' ').split()] for b in boards]
	# Keeping 1d boards, add 2d rep of boards, starting with rows
	boards = [[b, [b[i:i+5] for i in range(0, 25, 5)]] for b in boards]
	# Then columns
	for board in boards:
		board[1] += [[row[i] for row in board[1]] for i in range(5)]
	# Change rows and columns from lists to sets
	boards = [[b[0],[set(i) for i in b[1]]] for b in boards]


print(day4pt1(seq, boards))
print(day4pt2(seq, boards))