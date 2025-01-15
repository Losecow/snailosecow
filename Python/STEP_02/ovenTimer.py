H, M = map(int, input().split())
N = int(input())

if M + N >= 60:
    H += (M + N) // 60
    M = (M + N) % 60
    if H >= 24:
        H -= 24
    print(H, M)
else:
    print(H, M + N)
