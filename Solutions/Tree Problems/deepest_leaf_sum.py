# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        q = [root]
        
        while True:
            nq = list()
            for item in q:
                if item.left:
                    nq.append(item.left)
                if item.right:
                    nq.append(item.right)
            if nq == []:
                tot = 0
                for item in q:
                    tot+= item.val
                return tot
            else:
                q = nq