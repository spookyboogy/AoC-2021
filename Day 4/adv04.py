from itertools import combinations

def day4pt1():
	"""
	If you type and pronounce board enough times you being to question its spelling.
	"""
	
	with open('input.txt' , 'r') as f:
		f = f.read().split('\n\n')
		seq = [int(i) for i in f[0].split(',')]
		boards = [i.split('\n\n') for i in f[1:]]
	
	# Make each board into a 1d list of numbers
	boards = [[int(i) for i in b[0].replace('\n',' ').split()] for b in boards]
	# While keeping 1d boards, add board represented as rows
	boards = [[b, [b[i:i+5] for i in range(0, 25, 5)]] for b in boards]
	# Add board represented as columns to list of rows
	for board in boards:
		board[1] += [[row[i] for row in board[1]] for i in range(5)] 
	# Change the rows and columns from lists to sets
	boards = [[b[0],[set(i) for i in b[1]]] for b in boards]
	
	n = 5
	while n < len(seq):	
		for board in boards: 
			marked = [i for i in seq[:n] if i in board[0]]		
			if len(marked) > 4:
				bingo = [set(list(i)) for i in combinations(marked, 5)]
				for i in board[1]:
					if i in bingo:
						unmarked = [i for i in board[0] if i not in marked]
						return sum(unmarked) * seq[n-1]
		n += 1


def day4pt2():

	pass





print(day4pt1())
print(day4pt2())