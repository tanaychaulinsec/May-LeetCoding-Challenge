# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def bst(preorder,min,max):
            node=None
            if preorder and min<preorder[0]<max:
                node=TreeNode(preorder[0])
                del preorder[0]
                node.left=bst(preorder,min,node.val)
                node.right=bst(preorder,node.val,max)
            return node    
        return bst(preorder,-2**32,2**32)