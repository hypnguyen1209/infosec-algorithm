import math
a = 3458
b = 4864

def solve(a, b):
	d = math.gcd(a, b)
	if b == 0:
		return [d, 1, 0]
	x2 = 1
	x1 = 0
	y2 = 0
	y1 = 1
	while b > 0:
		q = math.floor(a/b)
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	return [a, x2, y2]

if __name__ == '__main__':
	print(solve(a, b))
