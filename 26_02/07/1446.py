import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    n, d = map(int, input().split())
    graph = [[] for _ in range(d + 1)]

    # 1. 기본 간선 추가 (i -> i+1 이동 비용은 1)
    for i in range(d):
        graph[i].append((i + 1, 1))

    # 2. 지름길 간선 추가
    for _ in range(n):
        s, e, l = map(int, input().split())
        if e <= d:
            graph[s].append((e, l))

    # 최단 거리 테이블
    dist = [float('inf')] * (d + 1) # 무한대로 초기화
    dist[0] = 0
    
    # 우선순위 큐 (거리, 현재노드)
    pq = [(0, 0)]

    while pq:
        current_dist, curr = heapq.heappop(pq)

        # 이미 더 짧은 경로를 찾았다면 패스
        if current_dist > dist[curr]:
            continue

        for next_node, weight in graph[curr]:
            cost = current_dist + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    print(dist[d])

dijkstra()