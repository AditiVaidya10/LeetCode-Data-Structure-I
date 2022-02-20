# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_, max_):
            if not node:
                return True
            if node.val <= min_ or node.val >= max_:
                return False
            left = validate(node.left, min_, node.val)
            right = validate(node.right, node.val, max_)
            return left and right
        return validate(root, float("-inf"), float("inf"))
