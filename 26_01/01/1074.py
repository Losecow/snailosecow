N, row, column = map(int, input().split())

def req(N, row, column):

	if N == 0:
		return 0
        
	return 2 * (row % 2)+(column % 2) + 4 * req(N - 1, int(row / 2), int(column / 2))

print(req(N, row, column))