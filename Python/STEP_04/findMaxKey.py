num = []
max = 0
count = 0
key = 0

while True:
    try:
        num.append(int(input()))
        if num[count] >= max:
            max = num[count]
            key = count + 1
        count += 1
    except:
        break

print(max)
print(key)
