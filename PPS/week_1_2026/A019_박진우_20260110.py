A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_str = str(result)

for i in range(10):
    print(result_str.count(str(i)))
