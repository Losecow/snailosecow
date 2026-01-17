n = int(input())

count_s = 100
count_c = 100
 
for i in range(n):
    chang, sang = map(int, input().split())

    if sang > chang:
        count_c -= sang
    elif sang < chang:
        count_s -= chang
    else:
        continue

print(count_c)
print(count_s)
