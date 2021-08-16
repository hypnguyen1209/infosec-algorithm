n = 877

def main():
    global n
    count = 0
    num = []
    index = []
    i = 2
    while n > 1:
        while n % i == 0:
            count = count + 1
            n = int(n / i)
        if count > 0:
            num.append(i)
            index.append(count)
            count = 0
        i = i + 1
    print(num)
    print(index)

if __name__ == '__main__':
    main()