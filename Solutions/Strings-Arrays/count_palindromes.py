class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None or s == "":
            return 0

        strings = 0
        length = len(s)

        # Odd length palindroms where each charachter might be the middle of th string
        for i in range(length):
            start = i
            end = i
            while s[start] == s[end]:
                strings += 1
                start -= 1
                end += 1
                if start < 0 or end >= length:
                    break

        # Even length palindromes
        for i in range(length-1):
            start = i
            end = i+1

            while s[start] == s[end]:
                strings += 1
                start -= 1
                end += 1
                if start < 0 or end >= length:
                    break

        return strings
