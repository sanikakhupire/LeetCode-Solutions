class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) 

        while left<right :
            mid = left + (right-left) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid+1

        return letters[left%len(letters)]