import math, re
a = 2147483646
b = 2147483643
p = 2147483647
w = 8
eps = 0
m = round(math.log2(p))
t = round(m / w)

def multiprecision_addition(a, b, w, t):
    global eps
    eps = 0
    c = [None for _ in a]
    a.reverse()
    b.reverse()
    for i in range(t):
        eps, c[i] = sumC(a[i], b[i])
    return eps, c[::-1]

def multiprecision_subtraction(a, b, w, t):
    global eps
    eps = 0
    c = [None for _ in a]
    a.reverse()
    b.reverse()
    for i in range(t):
        eps, c[i] = minusC(a[i], b[i])
    return eps, c[::-1]

def sumC(a, b):
    global eps
    re = a + b + eps
    k = pow(2, w)
    eps = 1 if re > k else 0
    c = re % k
    return eps, c

def minusC(a, b):
    global eps
    re = a - b - eps
    k = pow(2, w)
    eps = 1 if re < 0 else 0
    c = re % k
    return eps, c

def dec_to_int(l):
    n = ''.join([bin(i)[2:].zfill(8) for i in l])
    return int(n, 2)

def int_to_dec(n):
    n = bin(n)[2:].zfill(8*t)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]

def main():
    global a, b
    a = int_to_dec(a)
    b = int_to_dec(b)
    eps, c = multiprecision_addition(a, b, w, t)
    arr_p = int_to_dec(p)
    if eps == 0:
        if dec_to_int(c) < p:
            print(eps, c)
        else:
            eps = 0
            eps, d = multiprecision_subtraction(c, arr_p, w, t)
            print(eps, d)    
    else:
        eps = 0
        eps, d = multiprecision_subtraction(c, arr_p, w, t)
        print(eps, d)

if __name__ == '__main__':
    main()