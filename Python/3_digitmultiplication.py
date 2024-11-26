A = int(input())
B = int(input())

print(A * ((B - (B // 100 * 100)) % 10))
print(A * ((B - (B // 100 * 100)) // 10))
print(A * (B // 100))

print(A * B)
