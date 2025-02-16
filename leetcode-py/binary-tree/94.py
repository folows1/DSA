# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        return inorder(root)
    

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_rec(root, result):
            if root:
                inorder_rec(root.left, result)
                result.append(root.val)
                inorder_rec(root.right, result)
        
        result = []
        inorder_rec(root, result)
        return result

