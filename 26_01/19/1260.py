from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1 )]
visited_bfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)

ans_bfs = []
ans_dfs = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
for i in range(1, n+1): graph[i].sort()
# print(graph)

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True

    while q:
        node = q.popleft()
        ans_bfs.append(node)
        for next_node in graph[node]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                q.append(next_node)
    
    return ans_bfs



def dfs(start):

    visited_dfs[start] = True
    ans_dfs.append(start)

    for nxt in graph[start]:
        if not visited_dfs[nxt]:
            dfs(nxt)
    
    return ans_dfs





print(*dfs(v))
print(*bfs(v))