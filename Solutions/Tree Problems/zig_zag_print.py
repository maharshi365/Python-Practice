# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None

        out = list()
        q = [root]
        i = 1

        while len(q) > 0:
            if i == 1:
                out.append([x.val for x in q])
            else:
                out.append([x.val for x in reversed(q)])
            nq = list()
            for item in q:
                if item.left:
                    nq.append(item.left)
                if item.right:
                    nq.append(item.right)
            q = nq
            i = 1 - i

        return out
