# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # path sum 1
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False

        def _helper(curr, node):
            if node is None:
                return False

            curr -= node.val
            if node.left is None and node.right is None:
                if curr == 0:
                    return True
            else:
                return _helper(curr, node.left) or _helper(curr, node.right)

        return _helper(sum, root)
    # path sum 2

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        out = list()

        if root is None:
            return out

        def _helper(node, curr, path):
            if not node:
                return
            curr += node.val
            path = path + [node.val]

            if node.left is None and node.right is None and curr == sum:
                out.append(path)
            else:
                _helper(node.left, curr, path)
                _helper(node.right, curr, path)

        _helper(root, 0, [])
        return out
