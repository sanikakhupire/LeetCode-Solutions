class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = j = 0
        
        while j < len(haystack):

            if needle[i] == haystack[j]:
                i += 1
                j += 1

                if i == len(needle):
                    return j-i

            else:
                j = j - i + 1
                i = 0

        return -1
            