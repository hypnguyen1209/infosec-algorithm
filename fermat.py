t = 1
n = 1234
a = 2
def square_loop(a, k, n, t):
	b = 1
	if k == 0:
		return b
	c = a
	if k == 1:
		b = a
	for _ in range(t):
		c = pow(c, 2) % n
		if k == 1:
			b = c*b % n
	return b

def solve(a, n, t):
	r = square_loop(a, n - 1, n, t)
	for _ in range(t):
		if not r == 1:
			return 'HS'
	return 'NT'

if __name__ == '__main__':
 	print(solve(a, n, t)) 
