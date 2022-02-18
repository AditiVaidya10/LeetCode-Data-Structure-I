class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverseTree(root):
            if root:
                temp = root.right
                root.right = root.left
                root.left = temp
                self.invertTree(root.left)
                self.invertTree(root.right)
        traverseTree(root)
        return root
