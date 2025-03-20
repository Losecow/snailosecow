S = input()

result = [-1] * 26

for i in range(len(S)):
    if result[ord(S[i]) - ord('a')] == -1:
        result[ord(S[i]) - ord('a')] = i

print(*result)

레전드 코드

* 정석 코드

S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end=' ')
