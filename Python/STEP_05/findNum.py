dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())		
time = 0

for i in alpha:
    for j in dial:
        if i in str(j):
            time += dial.index(j) + 3
print(time)
