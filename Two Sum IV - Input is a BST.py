# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        s = set()
        while len(queue) > 0:
            current = queue.pop()
            if k-current.val in s:
                return True
            s.add(current.val)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return False
