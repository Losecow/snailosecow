import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    n, d = map(int, input().split())
    graph = [[] for _ in range(d + 1)]

    for i in range(d):
        graph[i].append((i + 1, 1))

    for _ in range(n):
        start, end, length = map(int, input().split())

    dist = [float('inf')] * (d + 1)
    dist[0] = 0

    pq = [(0, 0)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        # 현재의 경로가 dist 배열 속 현재부터의 경로보다 클 때
        if current_dist > dist[current]:
            # 무시
            continue

        # graph 배열 속 현재 위치 노드 값 (여러개일 수 있음)
        # 노드 값은 현재노드가 가리키는 다음 노드, 그 노드까지 이동하는 거리
        for next_node, weight in graph[current]:
            # cost = 이동하는 거리
            cost = current_dist + weight

            # 
            if cost < dist[next_node]:
                cost = current_dist + weight
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(pq, (cost, next_node))

    print(dist[d])

dijkstra()
