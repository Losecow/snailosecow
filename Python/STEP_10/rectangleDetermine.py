a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print("Equilateral")
elif a + b + c != 180:
    print("Error")
elif a == b or b == c or a == c:
    print("Isosceles")
elif a != b and b != c and a != c:
    print("Scalene")
