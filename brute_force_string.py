t = 'an tooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooan'
p = 'oan'

def solve(t, p):
	lent = len(t)
	lenp = len(p)
	for i in range(lent - lenp + 1):
		j = 0
		while j < lenp:
			if not p[j] == t[i + j]:
				break
			j += 1
		if j == lenp:
			return 'exist'
	return 'not exist'

if __name__ == '__main__':
	print(solve(t, p))