class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if A == [] or A[0] == [] or A is None:
            return None

        if len(A) == 1:
            return min(A[0])
        if len(A) == 3 and len(A[0]) == 1:
            return sum([A[0][i] for i in range(len(A))])

        # build up solution from bottom up to second row
        i = len(A) - 2
        while i >= 0:
            for j in range(1, len(A[i])-1):
                A[i][j] += min(A[i+1][j], A[i+1][j+1], A[i+1][j-1])
            # left edge
            A[i][0] += min(A[i+1][0], A[i+1][1])
            # right edge
            A[i][-1] += min(A[i+1][-1], A[i+1][-2])
            i -= 1

        return min(A[0])
