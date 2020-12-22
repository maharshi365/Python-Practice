
# https://leetcode.com/problems/validate-binary-search-tree/submissions/
# Medium Problem 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None: return True       
        out_list = list()
        
        def inorder(node):
            if node == None:
                pass
            else:
                inorder(node.left)
                out_list.append(node.val)
                inorder(node.right)
                
        inorder(root)
        
        for i in range(len(out_list)-1):
            if out_list[i] >= out_list[i+1]:
                return False
        
        return True

"""
O(n) time --> inorder traversal (all nodes in n time) + loop through to check (at max all nodes in (n-1) time) --> n+(n-1) = 2n-1 == O(n)
O(n) space --> inorder traversal to stor all node values
"""