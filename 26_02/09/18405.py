import sys
from collections import deque

# 빠른 입력을 위해 사용
input = sys.stdin.readline

# N: 시험관 크기, K: 바이러스 종류 수
n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, x축, y축) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 후 큐로 변환 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

# 목표 시간 S, 좌표 X, Y 입력
target_s, target_x, target_y = map(int, input().split())

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 시작
while q:
    virus, s, x, y = q.popleft()
    
    # S초가 지나면 반복문 종료
    if s == target_s:
        break
    
    # 현재 위치에서 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내에 있고 아직 전염되지 않은 경우
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

# 결과 출력 (좌표는 1부터 시작하므로 -1 해줌)
print(graph[target_x - 1][target_y - 1])