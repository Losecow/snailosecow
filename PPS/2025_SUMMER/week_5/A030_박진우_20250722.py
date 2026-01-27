N, first = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

good = 1.0 if first == 0 else 0.0
bad = 1.0 - good

for _ in range(N - 1):
    new_good = good * gg + bad * bg
    new_bad = good * gb + bad * bb
    good, bad = new_good, new_bad

print(round(good * 1000))
print(round(bad * 1000))
