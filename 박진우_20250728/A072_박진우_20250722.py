class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        # 윤년 판단 함수
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        # 각 달의 일수 (윤년일 때 2월은 29일)
        days_in_month = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        # 이전 달까지 일수 합 + 현재 일수
        return sum(days_in_month[:month - 1]) + day
