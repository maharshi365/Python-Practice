class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row = row + 1
            else:
                col = col - 1

        return False
