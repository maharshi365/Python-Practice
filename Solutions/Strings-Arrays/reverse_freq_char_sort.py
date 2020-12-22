class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        freq = dict()
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        
        sortedList = sorted(freq.items(),key = lambda x: x[1],reverse=True)
        
        return "".join(x[0]*x[1] for x in sortedList)
        