initials = sorted([input()[0] for _ in range(int(input()))])
unique = set(initials)
result = []
for ch in unique:
    if initials.count(ch) >= 5:
        result.append(ch)
print(''.join(sorted(result)) if result else "PREDAJA")
