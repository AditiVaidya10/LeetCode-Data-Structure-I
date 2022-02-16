class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return[]
        s=[]
        s+=(self.inorderTraversal(root.left))
        s+=[root.val]
        s+=(self.inorderTraversal(root.right))
        return s
