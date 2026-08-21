class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        max_c = 0

        for n in nums:
            if n == 1:
                c+=1
                max_c = max(c, max_c)
            else:
                c = 0
        return max_c