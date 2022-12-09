from sqlalchemy import true


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalpha())
        s = s.lower()
        length = len(s)//2 + 1
        s_length = len(s)
        if(s == " " or s == ""):
            return True
        for i in range(length):
            if s[i] != s[s_length-1]:
                return False
            s_length -= 1
        return True


message = " "
sol = Solution()
print(sol.isPalindrome(message))
