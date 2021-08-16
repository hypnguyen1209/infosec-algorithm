import math
n = 11 # n
t = 100 # số lần lặp t > 1 and t < n - 2

def square_loop(a, k, n):
    b = 1
    a %= n
    while k > 0:
        if k % 2 == 1:
            b = b*a % n
        k = math.floor(k/2)
        a = pow(a, 2) % n
    return b

def miller_rabin(n, t):
    if n < 2:
        return 'HS'
    if n - 2 < 2:
        return 'NT'
    s = 0
    r = n - 1 # n - 1 = 2^S*r r là lẻ
    while r % 2 == 0:
        r /= 2
        s += 1
    for i in range(t):
        a = 2
        y = square_loop(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y*y % n
                if y == 1:
                    return 'HS'
                j += 1
            if(y != n - 1):
                return 'HS'
    return 'NT'

def main():
    print(miller_rabin(n, t)) # xác xuất để số n sau t phép thử là số nguyên tố: 1 - (1/4)^t

if __name__ == '__main__':
    main()
