# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None: return True
        
        def _helper(node1,node2):
            if node1 is None and node2 is not None:
                return False
            elif node1 is not None and node2 is None:
                return False
            elif node1 is None and node2 is None:
                return True
            else:
                if node1.val == node2.val:
                    return (True and _helper(node1.left,node2.left) and _helper(node1.right,node2.right))
                else:
                    return False
        
        return _helper(p,q)