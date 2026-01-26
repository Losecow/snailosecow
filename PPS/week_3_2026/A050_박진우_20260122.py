s = input()
result = ""

for c in s:
    # 3칸 왼쪽으로 밀기 → ord('A') 기준으로 처리
    result += chr((ord(c) - ord('A') - 3) % 26 + ord('A'))

print(result)