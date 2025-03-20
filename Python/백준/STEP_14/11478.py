N = input()
total = set()
for i in range(len(N)):
    for j in range(i, len(N)):
        total.add(N[i : j + 1])

print(len(total))

# 슬라이싱 sample
# N = "hello"
# print(N[0:3])  # "hel"
# print(N[1:4])  # "ell"

# 슬라이싱한 문자열들을 집합에 넣어 중복 문자열을 제거