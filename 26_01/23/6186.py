# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# feild = [list(input().strip()) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if 0 <= nx < n and 0 <= ny < m:
#         if feild[nx][ny] == '.':
#             pass

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
