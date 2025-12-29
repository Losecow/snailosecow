n = int(input())

year = 2024
month = 1

total_month = (month - 1) + n * 7
year += total_month // 12
month = total_month % 12 + 1

print(year, month)
