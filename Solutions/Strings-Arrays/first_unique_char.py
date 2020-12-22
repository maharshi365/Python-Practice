class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == "": return -1
        
        seen = dict()
        
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char]+= 1
        
        for i, char in enumerate(s):
            if seen[char] == 1:
                return i
        
        return -1
        