import sys
input = sys.stdin.readline

N, K = map(int, input().split())

josephus = [i + 1 for i in range(N)]
result = []


# 리스트에서 원소를 계속 제거하기 때문에 순환 구조가 필요함
# 이에 따라, modulo 연산 (나머지연산) 이 필요함
idx = 0

for i in range(N):
    idx = (idx + K - 1) % len(josephus)
    result.append(josephus.pop(idx))

print("<", end = "")
for i in range(N - 1):
        print(result[i], ", ", sep = "", end = "")

print(result[N-1], ">", sep = "")

# 신기해서 가져옴 (deque)
# from collections import deque

# N, K = map(int, input().split())

# q = deque(range(1, N+1))
# result = []

# while q:
#     q.rotate(-(K-1))
#     result.append(q.popleft())

# print('<' + ", ".join(map(str, result)) + '>')