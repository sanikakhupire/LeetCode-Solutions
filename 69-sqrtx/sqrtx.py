class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        ans = 0
        while left<=right:
            mid = (left + right) // 2

            if (mid*mid) > x:
                right = mid - 1
            elif (mid*mid) <= x:
                ans = mid
                left = mid + 1
            
        return ans