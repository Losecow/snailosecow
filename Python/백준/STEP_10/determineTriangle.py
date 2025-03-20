while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif a + b + c <= 2 * max(a, b, c):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and b != c and a != c:
        print("Scalene")
    elif a == b or b == c or a == c:
        print("Isosceles")
