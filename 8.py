a = 45682375  
p = 489573857

def main():
    u = a
    v = p
    x1 = 1
    x2 = 0
    while (u != 1):
        q = v // u
        r = v - (q*u)
        x = x2 - (q*x1)
        v = u
        u = r
        x2 = x1
        x1 = x
    print(x1) 

if __name__ == '__main__':
    main()