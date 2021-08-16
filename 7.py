a = 28150488
b = 10507620

def main():
    if a == b:
        print(1)
        return
    u = a
    v = b
    e = 1
    while u % 2 == 0 and v % 2 == 0:
        u /= 2
        v /= 2
        e *= 2
    while not u == 0:
        if u % 2 == 0:
            u /= 2
        elif v % 2 == 0:
            v /= 2
        else:
            t = abs(u - v)/2
            if u < v:
                v = t
            else:
                u = t
    print(int(e*v))

if __name__ == '__main__':
    main()