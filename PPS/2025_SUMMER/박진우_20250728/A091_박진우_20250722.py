from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # 새 배열의 위치 포인터
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
