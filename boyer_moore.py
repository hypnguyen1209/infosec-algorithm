t = 'a pattern matching algorithm'
p = 'matchinga'

def last_occurrence(s):
	return p.rfind(s)

def solve(t, p):
	lent = len(t)
	lenp = len(p)
	jump = [lenp - 1]
	j = lenp - 1
	for i in range(lenp - 1, lent):
		if not i in jump:
			continue
		if not p[j] == t[i]:
			jump.append(i + lenp - min(j, 1 + last_occurrence(t[i])))
			j = lenp - 1
			continue
		if p[j] == t[i]:
			j -= 1
			i -= 1
			while j >= 0:
				if p[j] == t[i]:
					j -= 1
					i -= 1
				else:
					jump.append(i + lenp - min(j, 1 + last_occurrence(t[i])))
					j = lenp - 1
					break
				if j == 0:
					return 'exist'
	print('not exist')

if __name__ == '__main__':
	print(solve(t, p))