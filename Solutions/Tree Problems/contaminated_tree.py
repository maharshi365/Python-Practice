# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = {}
        self.lst[0] = True
        root.val = 0
        
        def _helper(node):
            if node is None:
                return
            if node.left:
                node.left.val = node.val*2 + 1
                self.lst[node.left.val] = True
            if node.right:
                node.right.val = node.val*2 + 2
                self.lst[node.right.val] = True
            _helper(node.left)
            _helper(node.right)
        
        _helper(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.lst


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)