for _ in range(int(input())):
    score = streak = 0
    for c in input():
        streak = streak + 1 if c == 'O' else 0
        score += streak
    print(score)
