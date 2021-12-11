def day8pt1(outputs):

	unique = [2, 4, 3, 7]
	return sum(sum(int(len(s) in unique) for s in i) for i in outputs)


def day8pt2(signals):
	
	def decipher(sigs, outs):

		num_segs = {str(i):'' for i in range(10)}
		for s in sigs + outs:
			if len(s) in unique.keys():
				num_segs[unique[len(s)]] = s
		for s in sigs + outs:
			if len(s) == 5: 
				dif = ''.join(i for i in num_segs['4'] if i not in num_segs['1'])
				if all(i in s for i in dif): 
					num_segs['5'] = s
				elif all(i in s for i in num_segs['1']): 
					num_segs['3'] = s
				else:
					num_segs['2'] = s
			elif len(s) == 6: 
				if all(i in s for i in num_segs['4']):
					num_segs['9'] = s
				elif all(i in s for i in num_segs['1']):
					num_segs['0'] = s
				else:
					num_segs['6'] = s
		return num_segs

	unique = {2:'1', 4:'4', 3:'7', 7:'8'}
	total = 0
	for i in range(len(signals)):
		sigs, outs = signals[i][0], signals[i][1]
		cipher = decipher(sigs, outs)
		n = ''
		for out in outs:
			for i in cipher.items():
				if all(s in i[1] for s in out) and len(out) == len(i[1]):
					n += i[0]
		total += int(n)
	return total


with open('input.txt', 'r') as f:
	f = f.read().splitlines()
	io = [line.split('|') for line in f]
	io = [[i[0].split(), i[1].split()] for i in io]

print(day8pt1([i[1] for i in io]))
print(day8pt2(io))