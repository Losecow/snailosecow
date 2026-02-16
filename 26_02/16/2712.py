import sys

def solve():
    # 입력 속도를 위해 sys.stdin.readline 사용
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        # 값과 단위를 분리하여 입력받음
        raw_val, unit = sys.stdin.readline().split()
        val = float(raw_val)
        
        # 단위에 따른 조건문 처리
        if unit == 'kg':
            result = val * 2.2046
            target_unit = 'lb'
        elif unit == 'lb':
            result = val * 0.4536
            target_unit = 'kg'
        elif unit == 'l':
            result = val * 0.2642
            target_unit = 'g'
        elif unit == 'g':
            result = val * 3.7854
            target_unit = 'l'
        
        # 소수점 4째자리까지 출력 (f-string 사용)
        print(f"{result:.4f} {target_unit}")

if __name__ == "__main__":
    solve()