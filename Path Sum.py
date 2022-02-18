class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def check(node, tmp):
            if node:
                if node.left:
                    node.left.val += node.val
                    check(node.left, tmp)
                if node.right:
                    node.right.val += node.val
                    check(node.right, tmp)
                elif not node.left:
                    tmp.append(node.val)
            return tmp
        
        if targetSum in check(root, []):
            return True
        else:
            return False
