import sys

input = sys.stdin.readline

# 1. 기다려야 하는 시간 T 입력
T = int(input())

# 2. 사탕의 개수 N 입력
N = int(input())

# 3. 사탕의 맛들 F_i 입력 (공백으로 구분된 리스트)
F = list(map(int, input().split()))

# 4. 사탕 맛의 총합 계산
total_flavor = sum(F)

# 5. 조건에 따른 결과 출력
if total_flavor >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")