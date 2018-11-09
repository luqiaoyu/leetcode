# 9. Palindrome Number

# Revert half of the number
# aware of overflow
# 300ms 59.73%
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False

        rev = 0
        while (x > rev):
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10
        

# convert to string, not recommended
# 436ms 31.64%
class Solution1:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        n = len(s)
        if n == 1: return True
        
        for i in range(n // 2):
            if (s[i] == s[n - 1 - i]):
                continue
            else:
                return False
            
        return True