T = 'NKANMANKKBAA'
P = 'KBAA'

def main():
    for i in range(len(T)):
        k = i
        for j in range(len(P)):
            if P[j] == T[k]:
                if j == len(P)-1:
                    print(True, k, i)
                    return
                k += 1
            else:
                break
    print(False, loop, -1)
    return 

if __name__ == '__main__':
    main() #tệ nhất: O(mn) trung bình O(m+n) hiệu quả vs bảng chữ cái lớn, khồng hiệu quả vs 0, 1 file ảnh....