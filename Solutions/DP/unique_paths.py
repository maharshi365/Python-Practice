class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        grid = [[None for x in range(m)] for y in range(n)]
        
        for i in range(len(grid[0])):
            grid[0][i] = 1
        
        for i in range(len(grid)):
            grid[i][0] = 1
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        
        grid = [[None for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))]
        
        grid[0][0] = 1
        
        #fill top row
        for i in range(len(grid[0])):
            if obstacleGrid[0][i] == 0:
                grid[0][i] = 1
            else:
                grid[0][i] = 0
                break
        # fill rest of top row if obstacle in top row
        try:
            for elem in range(i+1,len(grid[0])):
                grid[0][elem] = 0
        except:
            pass
        
        
        # fill leftmost column
        for i in range(len(grid)):
            if obstacleGrid[i][0] == 0:
                grid[i][0] = 1
            else:
                grid[i][0] = 0
                break
        # fill rest of leftmost column if obstacle in leftmost col
        try:
            for elem in range(i+1,len(grid)):
                grid[elem][0] = 0
        except:
            pass
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]


