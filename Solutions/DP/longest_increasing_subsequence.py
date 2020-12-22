class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == [] or nums is None:
            return 0

        s = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and s[j] + 1 > s[i]:
                    s[i] = s[j] + 1

        return max(s)
