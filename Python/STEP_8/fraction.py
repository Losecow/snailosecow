N = int(input())

temp = N

cnt = 1
while True:
    if temp - cnt <= 0:
        break
    temp -= cnt
    cnt += 1

numerator = 0
denominator = 0

if cnt % 2 == 0:
    for i in range(temp):
        numerator = i + 1 
        denominator = cnt - i


elif cnt % 2 != 0:
    for i in range(temp):
        numerator = cnt - i
        denominator = i + 1 

print(numerator, "/", denominator, sep = "")