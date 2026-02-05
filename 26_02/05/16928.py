import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # N: 사다리 수, M: 뱀의 수
    n, m = map(int, input().split())
    
    # 1부터 100까지의 보드판 생성 (이동할 위치를 저장)
    board = [i for i in range(101)]
    
    # 사다리와 뱀 정보 입력 (도착 지점을 업데이트)
    for _ in range(n + m):
        u, v = map(int, input().split())
        board[u] = v
        
    # 방문 여부 및 주사위 횟수 저장 (-1은 미방문)
    visited = [-1] * 101
    
    # BFS 시작
    queue = deque([1])
    visited[1] = 0 # 시작점 횟수는 0
    
    while queue:
        curr = queue.popleft()
        
        # 100번 칸에 도착하면 결과 출력 후 종료
        if curr == 100:
            print(visited[curr])
            break
            
        # 주사위 1~6 굴리기
        for dice in range(1, 7):
            next_pos = curr + dice
            
            if next_pos <= 100:
                # 사다리나 뱀을 타고 이동할 최종 목적지 확인
                destination = board[next_pos]
                
                # 아직 방문하지 않은 칸이라면
                if visited[destination] == -1:
                    visited[destination] = visited[curr] + 1
                    queue.append(destination)


solve()