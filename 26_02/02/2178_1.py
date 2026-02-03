import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]

print(bfs(0, 0))