class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        check = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        ans = []

        for i in s:
            
            if i not in check:
                ans.append(i)

            elif ans and check[i] == ans[-1]:
                ans.pop()
            else:
                return False

        if not ans:
            return True
        else:
            return False

