num = input()
counts = [0] * 10

for c in num:
    counts[int(c)] += 1

# 6과 9는 합쳐서 처리
counts[6] = (counts[6] + counts[9] + 1) // 2
counts[9] = 0

print(max(counts))
