class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        li = [0]*(n+1)

        for i in nums:
            li[i] += 1
        
        ans = []
        for i in range(1,n+1):
            if li[i] == 0:
                ans.append(i)
        
        return ans