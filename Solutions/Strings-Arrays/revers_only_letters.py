class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S is None: return None
        if S == "": return ""
        
        def validLetter(c):
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                return True
            else:
                return False
        
        
        string = list(S)
        
        i, j = 0, len(S) - 1
        
        while i < j:
            if not validLetter(string[i]):
                i+=1
                continue
            if not validLetter(string[j]):
                j-=1
                continue
            string[i],string[j] = string[j],string[i]
            i+=1
            j-=1
        
        return "".join(string)