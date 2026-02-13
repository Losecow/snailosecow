import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 도시 개수, M: 도로 개수, K: 타겟 거리, X: 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화 (-1은 방문하지 않음을 의미)
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0

# BFS 수행
queue = deque([x])
while queue:
    now = queue.popleft()
    
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신 (현재 거리 + 1)
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 K인 모든 도시 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if not check:
    print(-1)