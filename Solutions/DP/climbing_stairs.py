class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 0: return None
        if n == 0: return 0
        
        memo = dict()
        
        
        def _helper(numSteps):
            if numSteps < 0:
                return 0
            elif numSteps == 0:
                return 1
            else:
                if (numSteps) in memo:
                    return memo[numSteps]
                
                memo[numSteps] = _helper(numSteps-1) + _helper(numSteps-2)
                return memo[numSteps]
        
        
        
        return _helper(n)