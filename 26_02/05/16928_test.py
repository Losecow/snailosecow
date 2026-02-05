import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    board = [i for i in range(101)]

    for _ in range(n + m):
        u, v = map(int, input().split())
        board[u] = v
    
    visited = [-1] * 101

    queue = deque([1])
    visited[1] = 0

    while queue:
        curr = queue.popleft()

        if curr == 100:
            print(visited[curr])
            break
    
        for dice in range(1, 7):
            next_pos = curr + dice

            if next_pos <= 100:
                destination = board[next_pos]

                if visited[destination] == -1:
                    visited[destination] = visited[curr] + 1
                    queue.append(destination)
solve()