# 7. Reverse Integer

# 52ms 99.19%
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        flag = (x > 0)
        x = abs(x)
        while (x != 0):
            pop = x % 10
            x = x // 10
            if flag:
                if (rev > 2147483647 // 10 or (rev == 2147483647 // 10 and pop > 7)):    # 一定要用2**31 - 1不能用sys.maxsize
                    return 0
            else:
                if (rev > 2147483647 // 10 or (rev == 2147483647 // 10 and pop > 8)):
                    return 0
            rev = rev * 10 + pop
        
        return rev if flag else -rev