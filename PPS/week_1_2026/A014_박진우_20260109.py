class Solution:
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res

        start = nums[0]
        for i in range(1, len(nums)):
            # 연속되지 않는 순간
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i-1]}")
                start = nums[i]

        # 마지막 구간 처리
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res
