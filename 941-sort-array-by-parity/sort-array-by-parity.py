class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left, right = 0, len(nums)-1

        while left<right:
            if (nums[left] % 2) != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
            else:
                left+=1

        return nums