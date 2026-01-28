import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]

# 정육각형 6방향
dirs_even = [(-1,-1), (-1,0), (0,-1), (0,1), (1,-1), (1,0)]
dirs_odd  = [(-1,0),  (-1,1), (0,-1), (0,1), (1,0),  (1,1)]

ans = 0

for y in range(N):
    for x in range(M):
        dirs = dirs_even if y % 2 == 0 else dirs_odd

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                # (y,x) < (ny,nx) 일 때만 카운트 → 중복 방지
                if (y, x) < (ny, nx):
                    if A[y][x] != A[ny][nx]:
                        ans += 1

print(ans)
