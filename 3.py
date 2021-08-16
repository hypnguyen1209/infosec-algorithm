import math
a = 38762497#[2, 79, 120, 1]
b = 568424364#[33, 225, 119, 172]
w = 8
t = 4
eps = 0
def main(a, b, w, t):
    c = [None for _ in a]
    a.reverse()
    b.reverse()
    for i in range(t):
        eps, c[i] = minusC(a[i], b[i])
    print((eps, tuple(c[::-1])))

def minusC(a, b):
    global eps
    re = a - b - eps
    k = pow(2, w)
    eps = 1 if re < 0 else 0
    c = re % k
    return eps, c

def dec_to_arr(w, F, a):
    result = []
    m = round(math.log2(F))
    t = round(m / w)
    n = [pow(2, i*w) for i in range(t)[::-1]]
    for i in n:
        result.append(math.floor(a/i))
        a %= i
    return result

if __name__ == '__main__':
    aa = dec_to_arr(w, 2147483647, a) # aa = a
    bb = dec_to_arr(w, 2147483647, b) # bb = b
    main(aa, bb, w, t)