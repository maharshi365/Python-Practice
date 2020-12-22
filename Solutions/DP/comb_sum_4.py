class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        memo = dict()

        def _helper(n):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                if n in memo:
                    return memo[n]
                else:
                    tot = 0
                    for num in nums:
                        tot += _helper(n-num)
                    memo[n] = tot
                    return tot

        return _helper(target)
