N, M = map(int, input().split())

if N < M: # 합보다 차가 큰 경우를 제외하면 (s+m < 0 , s-m < 0) 경우가 모두 제외된다
    print(-1)
else:
    A = (N + M) // 2
    B = (N - M) // 2
    if (A + B) == N and (A - B) == M : 
        print(A, B)
    else:
        print(-1)
