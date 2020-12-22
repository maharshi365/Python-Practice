class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None or s == "":
            return 0

        codes = {str(i): True for i in range(1, 27)}

        memo = dict()

        def _helper(chars):
            if chars == '0':
                return 0
            if len(chars) <= 1:
                return 1
            if chars in memo:
                return memo[chars]
            else:
                tot = 0
                if chars[0] in codes:
                    tot += _helper(chars[1:])
                if chars[:2] in codes:
                    tot += _helper(chars[2:])
                memo[chars] = tot
                return tot

        return _helper(s)
