import sys

# 입력을 빠르게 받기 위해 사용
N, M = map(int, sys.stdin.readline().split())
floor = [input() for _ in range(N)]

count = 0

# 1. 가로 판자 '-' 개수 세기
for i in range(N):
    is_row = False # 가로 판자가 이어지고 있는지 확인하는 플래그
    for j in range(M):
        if floor[i][j] == '-':
            if not is_row: # 새로운 '-' 판자의 시작점이라면
                count += 1
                is_row = True
        else: # '|'를 만나면 가로 판자 흐름이 끊김
            is_row = False

# 2. 세로 판자 '|' 개수 세기
for j in range(M):
    is_col = False # 세로 판자가 이어지고 있는지 확인하는 플래그
    for i in range(N):
        if floor[i][j] == '|':
            if not is_col: # 새로운 '|' 판자의 시작점이라면
                count += 1
                is_col = True
        else: # '-'를 만나면 세로 판자 흐름이 끊김
            is_col = False

print(count)