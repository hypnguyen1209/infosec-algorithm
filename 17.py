T = 'abacaabadcabacabaabb'
P = 'abaa'

def lps(P):
    l = len(P)
    i = 0
    j = 1
    arr = [0 for _ in range(l)]
    while j < l:
        if P[i] == P[j]:
            arr[j] = i + 1
            i += 1
            j += 1
        elif i == 0:
            arr[j] = 0
            j += 1
        else:
            i = arr[i - 1]
    return arr

def KMP(T, P):
    l = lps(P)
    m = len(P)
    n = len(T)
    i = 0
    j = 0
    count = 0
    while (i < n):
        count += 1
        if (P[j] == T[i]):
            i += 1
            j += 1
        if(j == m):
            return (True, count, i - j)
        elif(i < n and P[j] != T[i]):
            if(j != 0):
                j = l[j - 1]
            else:
                i+=1
    return (False, count, -1)

def main():
    print(KMP(T, P)) # O(m+n)

if __name__ == '__main__':
    main()