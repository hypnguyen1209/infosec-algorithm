a = 5
k = 596
n = 1234
def solve(a, k, n):
	b = 1
	if k == 0:
		return b
	c = a
	if k == 1:
		b = a
	while True:
		c = pow(c, 2) % n
		if k == 1:
			b = c*b % n
			return b

if __name__ == '__main__':
	print(solve(a, k, n))
