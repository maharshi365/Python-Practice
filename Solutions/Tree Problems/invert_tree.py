# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None: return root
        
        def _helper(node):
            if node is None:
                return 
            else:
                if node.left or node.right:
                    node.left, node.right = node.right, node.left
                    _helper(node.left)
                    _helper(node.right)
                else:
                    return
                
        _helper(root)
        
        return root