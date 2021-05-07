import math

a = 30
p = 101

def solve(a, p):
	u = a
	v = p
	x1 = 1
	x2 = 0
	while not u == 1:
		q = math.floor(v/u)
		r = v - q*u
		x = x2 - q*x1
		v = u
		u = r
		x2 = x1
		x1 = x
	if x1 < 0:
		x1 += p
	return [x1, p]

if __name__ == '__main__':
	print(solve(a, p))