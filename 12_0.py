import math

n = 213
def main():    
    if(n < 2):
        print('HS')
    else:
        check = True
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                check = False
                break
        if check:
            print('NT')
        else:
            print('HS')

if __name__ == '__main__':
    main()