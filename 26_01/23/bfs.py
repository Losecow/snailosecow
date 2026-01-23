from collections import deque

visited = [False] * (n+1)
queue = deque([start])
visited[start] = True

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            queue.append(nxt)
