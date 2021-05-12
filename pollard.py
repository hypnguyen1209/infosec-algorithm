n = 455459

def gcd(a, b):
	while b > 0:
		r = a % b
		a = b
		b = r
	return a

def solve(n):
	a = 2
	b = 2
	while True:
		a = (pow(a, 2) + 3) % n
		b = (pow(b, 2) + 3) % n
		b = (pow(b, 2) + 3) % n
		d = gcd(a - b, n)
		if 1 < d and d < n:
			return d
		if d == n:
			exit()

if __name__ == '__main__':
	print(solve(n))