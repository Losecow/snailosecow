month = int(input())
day = int(input())

if month == 2:
  if day == 18:
    print('Special')
  elif day < 18:
    print('Before')
  else:
    print('After')
elif month < 2:
  print('Before')
else:
  print('After')
