n = 43567127

def GCD(x, y):
    if (x == y):
        return 1
    while(y != 0):
        tmp = x % y
        x = y
        y = tmp
    return x
def main():
    a = 2
    b = 2
    while True:
        a = (a**2+1) % n
        b = (b**2+1) % n
        b = (b**2+1) % n
        d = GCD(a-b, n)
        if (1 < d and d < n):
            print(d)
            return
        if d == n:
            return False
if __name__ == '__main__':
    main()