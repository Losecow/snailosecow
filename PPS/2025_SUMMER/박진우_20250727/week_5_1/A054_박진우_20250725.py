def solution(board, moves):
    basket = []
    count = 0

    for move in moves:
        col = move - 1  # 인덱스 조정
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0  # 뽑았으니 제거
                if basket and basket[-1] == doll:
                    basket.pop()
                    count += 2  # 터졌으므로 2점
                else:
                    basket.append(doll)
                break  # 뽑았으면 다음 move로
    return count
