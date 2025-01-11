a, b, c = map(int, input().split())

minT = min(a, b, c)
maxT = max(a, b, c)
midT = a + b + c - minT - maxT

if maxT > midT - minT:
    if maxT >= midT + minT:
        maxT = midT + minT - 1

print(minT + maxT + midT)
