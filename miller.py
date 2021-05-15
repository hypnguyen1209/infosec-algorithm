import math
n = 91 # n>= 3
t = 1 # n >= 1
a = [2]

def square_loop(a, k, n):
	b = 1
	a %= n
	while k > 0:
		if k % 2 == 1:
			b = b*a % n
		k = math.floor(k/2)
		a = pow(a, 2) % n
	return b

def solve(n, t, a):
	r = (n - 1)/2
	for i in range(t):
		y = square_loop(a[i], r, n)
		if not y == 1 and not y == n - 1:
			j = 1
			while j <= 0 and not y == n - 1:
				y = pow(y, 2) % n
				if y == 1:
					return 'HS'
				j += 1
			if not y == n - 1:
				return 'HS'
	return 'NT'

if __name__ == '__main__':
	print(solve(n, t, a))

