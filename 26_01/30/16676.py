N = int(input())

answer = 0
num = 0

while True:
    num = num * 10 + 1  # 1, 11, 111, 1111 ...
    if num > N:
        break
    answer += 1

print(answer)
