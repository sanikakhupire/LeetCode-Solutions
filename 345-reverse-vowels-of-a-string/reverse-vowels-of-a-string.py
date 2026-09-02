class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        left = 0
        right = len(s) - 1
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])

        li = list(s)

        while left<right:
            while left<right and s[left] not in vowels:
                left += 1
            
            while left<right and s[right] not in vowels:
                right -= 1

            li[left] , li[right] = li[right], li[left]
            left += 1
            right -= 1

        return "".join(li)
        