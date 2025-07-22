class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            original = num
            while num != 0:
                digit = num % 10
                if digit == 0 or original % digit != 0:
                    break
                num //= 10
            else:
                result.append(original)
        return result
 