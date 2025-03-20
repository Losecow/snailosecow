N = int(input())

temp = 0
cnt = 0

while True:
    if N > temp:
        temp += 1
        N = N - temp
        cnt += 1
    else:
        print(cnt)
        break