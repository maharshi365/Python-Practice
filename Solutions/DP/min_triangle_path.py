class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        if triangle is None: return None
        if triangle[0] == []: return None
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        if len(triangle) == 2:
            return min([x+triangle[0][0] for x in triangle[1]])
        
        i = len(triangle) - 2 
        while i > 0:
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]) 
            i -= 1
        
        return min(triangle[1]) + triangle[0][0]