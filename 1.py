import math
w = 8
F = 2147483647
a = 38762497

def main(w, F, a):
    result = []
    m = round(math.log2(F))
    t = round(m / w)
    n = [pow(2, i*w) for i in range(t)[::-1]]
    for i in n:
        result.append(math.floor(a/i))
        a %= i
    print(result)

if __name__ == '__main__':
    main(w, F, a)