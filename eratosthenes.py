n = 524288

def solve(n):
	result = []
	p = 2
	num_list = [True for _ in range(n + 1)]
	while n >= pow(p, 2):
		if num_list[p]:
			for i in range(2*p, n + 1, p):
				num_list[i] = False
		p += 1
	
	for i in range(n + 1):
		if i >= 2 and num_list[i]:
			result.append(i)
	return len(result)
	
if __name__ == '__main__':
	print(solve(n))