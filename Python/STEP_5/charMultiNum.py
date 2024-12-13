N = int(input())

for _ in range(N):
    num, arr = input().split()
    num = int(num)
    result = ""
    for char in arr:
        result += char * num  # 각 문자를 num만큼 반복
    print(result)
