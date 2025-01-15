N = input()

N = N.upper()

Member = ''.join(set(N))
count = []

Max = 0
tmp = ''
for i in range(len(Member)):
    count.append(N.count(Member[i]))
    if count[i] > Max:
        Max = count[i]
        tmp = Member[i]
    elif count[i] == Max:
        tmp = '?'

print(tmp)

# 조금 더 줄여보면

N = input().upper()

Member = ''.join(set(N))
count = []

Max = 0
tmp = ''
for i in range(len(Member)):
    count.append(N.count(Member[i]))
    if count[i] > Max:
        Max = count[i]
        tmp = Member[i]
    elif count[i] == Max:
        tmp = '?'

print(tmp)
