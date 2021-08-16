import math
import random 

n = 13
t = 2

def square_loop(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    if k&1 == 1:
        b = a 
    for i in range (1, len(bin(k))-2):
        A = (A**2)%n 
        if (k >> i)&1 == 1:
            b = (A*b) % n 
    return b

def Fermat(n,t):
    for i in range(1, t+1):
        a = random.randint(2, n-2)
        r = square_loop(a, n-1, n)
        if r != 1:
            return 'HS'
    return 'NT'

def main():
    print(Fermat(n, t))

if __name__ == "__main__":
    main()