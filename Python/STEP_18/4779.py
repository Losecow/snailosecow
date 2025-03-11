def cantor(A, start, last):
    
    if last - start > 2:
        
        mid1 = (last - start) // 3 + start
        mid2 = (last - start) * 2 // 3 + start

        for i in range(mid1, mid2):
            A[i] = " "
        
        cantor(A, start, mid1)
        cantor(A, mid1,  mid2) # 없어도 ㄱㅊ
        cantor(A, mid2,  last)

    else:
        return A

while True:
    try:
        N = int(input())

        A = ["-" for _ in range(3**N)]
        start = 0
        last = len(A)

        cantor(A, start, last)

        print(*A, sep = "")
    except:
        break