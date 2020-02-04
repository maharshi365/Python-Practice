class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N < 0: return None
        
        fib = [0,1]
        
        if N < 2:
            return fib[N]
        
        N = N - 1
        while(N > 0):
            last = fib[-1]+fib[-2]
            fib.append(last)
            N-=1
        
        return fib[-1]