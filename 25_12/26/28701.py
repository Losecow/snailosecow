n = int(input())

result = 0

if n % 2 == 0:
    result = (n + 1) * int(n / 2)
else:
    result = (n + 1) * int(n / 2) + int(n / 2) + 1

print(result)
print(result * result)

result = 0

for i in range(1, n + 1):
    result += i * i * i 

print(result)