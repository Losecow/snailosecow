# 내 코드

N = input()

tmp = N[::-1]
cnt = 0

for i in range(len(N)):
    if N[i] != tmp[i]:
        cnt += 1
    else:
        continue

if cnt != 0:
    print("0")
else:
    print("1")

# 답 코드 중 가장 마음에 든 코드

s = input().strip()
if s == s[::-1]:
    print(1)
else:
    print(0)

