T = int(input())
Coin = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    for i in range(len(Coin)):
        print(int(C / Coin[i]), end = " ")
        C = C % Coin[i]