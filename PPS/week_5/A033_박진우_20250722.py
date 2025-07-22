max_score = 0
winner = 0

for i in range(1, 6):  # 참가자는 1번부터 5번
    scores = list(map(int, input().split()))
    total = sum(scores)
    if total > max_score:
        max_score = total
        winner = i

print(winner)
print(max_score)
