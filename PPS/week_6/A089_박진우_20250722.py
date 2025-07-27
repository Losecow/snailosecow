from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None

        mid = len(nums) // 2
        node = TreeNode(nums[mid])  # 리트코드 내장 TreeNode 사용

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node
