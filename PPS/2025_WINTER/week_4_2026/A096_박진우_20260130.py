class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # 1비트를 하나 제거
            count += 1
        return count
