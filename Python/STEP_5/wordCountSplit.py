# 블랭크의 갯수를 세되, 처음이나 마지막에 블랭크가 아닐 경우 + 1 해주는 코드

N = str(input())
cnt = 0

if N[0] != " ":
    if N[len(N) - 1] != " ":
        cnt += 1

if N[0] == " ":
    if N[len(N) - 1] == " ":
        cnt -= 1

for i in range(len(N)):
    if N[i] == " ":
        cnt += 1

print(cnt)


# 정답 풀이
# 사실 이렇게 풀면 된다

# print(len(input().split())
# 망할...
