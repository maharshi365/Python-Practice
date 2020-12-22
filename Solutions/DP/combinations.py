class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        
        out = list()
        
        def _helper(left,curr):
            if len(curr) == k:
                out.append(curr)
                return
            
            for i in range(left,n+1):
                _helper(i+1,curr + [i])
        
        _helper(1,[])
        
        return out
            
            
                    