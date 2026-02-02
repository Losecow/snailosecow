import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])
    
    # 이동할 네 가지 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위를 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 벽(0)인 경우 무시
            if maze[nx][ny] == 0:
                continue
                
            # 처음 방문하는 길(1)인 경우에만 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    # 마지막 칸까지의 최단 거리 반환
    return maze[N-1][M-1]

print(bfs(0, 0))