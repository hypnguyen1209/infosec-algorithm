T = 'abacaabadcabacabaabb'
P = 'def'

def last_occurrence(T, P):
    for i in range(len(P) - 1, -2, -1):
        if i == -1:
            return -1
        if T == P[i]:
            return i

def boyer_moore(T, P):
    m = len(P)
    n = len(T)
    i = m - 1
    j = m - 1
    count = 0
    while i < n:
        count += 1
        if T[i] == P[j]:
            if j == 0: 
                return (True, count, i)
            i -= 1
            j -= 1
        else:
            l = last_occurrence(T[i], P)
            i +=  m - min(j, 1 + l)
            j = m - 1
    return (False, count, -1)


def main():
    print(boyer_moore(T, P))

if __name__ == '__main__':
    main()
