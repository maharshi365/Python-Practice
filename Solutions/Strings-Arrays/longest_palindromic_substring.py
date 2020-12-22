class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == "": return ""
        if s == None: return None
        
        maxFound = s[0]
        maxLen = 1
        s_len = len(s)
        #odd length palindromes
        for i in range(len(s)):
            l = 0
            r = 0
            curr = 1
            while True:
                l-=1
                r+=1
                if (l+i) < 0 or (r+i) > s_len - 1:
                    break
                elif s[l+i] == s[r+i]:
                    curr += 2
                    if curr > maxLen:
                        maxLen = curr
                        maxFound = s[l+i:r+i+1]
                else:
                    break
        
        #even length palindromes
        for i in range(len(s)-1):
            l = 0
            r = 1
            if s[i+l] == s[i+r]:
                curr = 2
                if curr > maxLen:
                    maxLen = curr
                    maxFound = s[l+i:r+i+1]
            else:
                continue
            while True:
                l-=1
                r+=1
                if (l+i) < 0 or (r+i) > s_len - 1:
                    break
                elif s[l+i] == s[r+i]:
                    curr += 2
                    if curr > maxLen:
                        maxLen = curr
                        maxFound = s[l+i:r+i+1]
                else:
                    break
                    
        return maxFound
