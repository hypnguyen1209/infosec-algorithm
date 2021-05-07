import math, re

a = [0, 11, 173, 248] 
b = [0, 1, 226, 64]
W = 8
p = 2147483647

def int_to_dec(n, f):
	n = bin(n)[2:].zfill(f)
	b = re.findall('\d{8}', n)
	c = ['0b' + i for i in b]
	return [int(i, 2) for i in c]

def solve(a, b, W, p):
	a.reverse()
	b.reverse()
	m = round(math.log2(p))
	t = round(m/W)
	c = [0 for i in range(2*t)]
	for i in range(t):
		u = 0
		for j in range(t):
			uv = c[i + j] + a[i]*b[j] + u
			[u, v] = int_to_dec(uv, 16)
			c[i + j] = v
		c[i + t] = u
	return c[::-1]

if __name__ == '__main__':
	print(solve(a, b, W, p))