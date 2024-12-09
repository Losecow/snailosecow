N, M = map(int, input().split())

arr = [i + 1 for i in range(N)]

for _ in range(M):  # M번의 입력을 처리
    A, B = map(int, input().split())
    # A-1부터 B-1까지를 뒤집음
    arr[A-1:B] = arr[A-1:B][::-1]

print(*arr)
