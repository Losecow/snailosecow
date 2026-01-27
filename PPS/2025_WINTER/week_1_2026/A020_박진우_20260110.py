max_people = 0
current = 0

for _ in range(4):
    out_num, in_num = map(int, input().split())
    current -= out_num
    current += in_num
    if current > max_people:
        max_people = current

print(max_people)
