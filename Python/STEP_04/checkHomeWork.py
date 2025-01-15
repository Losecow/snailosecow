student=[i + 1 for i in range(30)]

for i in range(28):
    data=int(input())
    student.remove(data)
    
print(min(student))
print(max(student))
