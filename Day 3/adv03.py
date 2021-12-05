def day3pt1(report):

	rlen = len(report) 
	bits = min(list(set(len(i) for i in report)))
	cols = [[int(row[col]) for row in report] for col in range(bits)]
	gam = ''.join(str(int(sum(col) > (rlen / 2) - 1)) for col in cols)
	eps = ''.join(str(int(sum(col) < rlen / 2)) for col in cols)

	return int(gam, 2) * int(eps, 2)


def day3pt2(report):

	oxy, co2 = report, report

	pos = 0
	while len(oxy) > 1:
		cols = [int(n[pos]) for n in oxy]
		crit = str(int(sum(cols) >= len(oxy) / 2))
		oxy = [n for n in oxy if n[pos] == crit]
		pos += 1
	
	pos = 0
	while len(co2) > 1:
		cols = [int(row[pos]) for row in co2]
		crit = str(int(sum(cols) < len(co2) / 2))
		co2 = [n for n in co2 if n[pos] == crit]
		pos += 1
			
	return int(oxy[0], 2) * int(co2[0], 2)
	

with open('input.txt', 'r') as f:
		report = f.read().splitlines()		

print(day3pt1(report))
print(day3pt2(report))