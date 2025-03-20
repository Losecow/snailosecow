import sys
input = sys.stdin.readline

N = int(input())

# 엑셀로 정리해봤는데 제곱수가 살아남음
# 루트 N 구하면 될듯

M = int(N ** (1 / 2))

print(M)