import math, re

a = 524647
b = 32549
W = 8
p = 2147483647

def int_to_dec(n, f):
    n = bin(n)[2:].zfill(f)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]

def dec_to_array(w, F, a):
    result = []
    m = round(math.log2(F))
    t = round(m / w)
    n = [pow(2, i*w) for i in range(t)[::-1]]
    for i in n:
        result.append(math.floor(a/i))
        a %= i
    return result
a = dec_to_array(W, p, a)
b = dec_to_array(W, p, b)

def main(a, b, W, p):
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
    print(c[::-1]) 

if __name__ == '__main__':
    main(a, b, W, p)     