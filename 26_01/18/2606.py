from collections import deque

node = int(input())
line = int(input())

net = [[] for _ in range(node + 1)]

for _ in range(line):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)


visited = [False] * (node + 1)

queue = deque([1])
visited[1] = True
count = 0

while queue:
    cur = queue.popleft()

    for next in net[cur]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            count += 1

print(count)

