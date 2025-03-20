import sys
input = sys.stdin.readline

# dictionary 사용
d = {}
count = 0
n, m = map(int, input().split())

for _ in range(n):
    data = input().rstrip() 
    d[data] = True

for _ in range(m):
    data = input().rstrip()
    if data in d:
        count += 1

print(count)

# rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# 인자가 없을 경우 오른쪽 공백 제거
# 'apple'.rstrip('lep')    # 오른쪽으로 l, e, p의 문자열의 모든 조합을 제거 -> 'a'


