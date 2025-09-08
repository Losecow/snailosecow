class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return (root.val +
                    self.rangeSumBST(root.left, low, high) +
                    self.rangeSumBST(root.right, low, high))
