class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        out = []
        if nums is None or nums == []:
            return []

        def _helper(curr, items):
            if len(items) == 1:
                out.append(curr+items)

            for i in range(len(items)):
                newL = items[:i] + items[i+1:]
                new_curr = curr + [items[i]]
                _helper(new_curr, newL)

        _helper([], nums)

        return out
