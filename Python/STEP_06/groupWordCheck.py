N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:

#word[j]의 다음 인덱스부터 끝까지 모든 문자를 포함하는 부분 문자열을 의미

            cnt -= 1
            break

print(cnt)

