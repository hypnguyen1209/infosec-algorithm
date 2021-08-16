import math
n = 22

def GCD(x: int, y: int) -> int:
    if x == y:
        return 1
    while y != 0:
        tmp = x % y
        x = y
        y = tmp
    return x

def prime_number(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def camichael(n: int) -> bool:
    if prime_number(n) and n < 2:
        return False
    for i in range(2, n):
        if GCD(i, n) == 1:
            if pow(i, n - 1) % n != 1:
                return False
    return True

def main():
    print('camichael' if camichael(n) else 'no camichael')

if __name__ == '__main__':
    main()