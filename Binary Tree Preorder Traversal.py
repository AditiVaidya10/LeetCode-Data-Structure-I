class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res+= [root.val]
            res+= self.preorderTraversal(root.left)
            res+= self.preorderTraversal(root.right)
        return res
