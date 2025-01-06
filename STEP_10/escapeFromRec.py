location = list(map(int, input().split()))

location.append(abs(location[0] - location[2]))
location.append(abs(location[1] - location[3]))

print(min(location))