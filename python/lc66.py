# 66. Plus One

# 60ms 19.56% O(n)
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        i = n - 1
        while (carry != 0 and i >= 0):
            res = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = res
            i -= 1

        if carry == 0:
            return digits
        else:
            digits = [carry] + digits
            return digits

# 60ms 19.56%
class Solution1:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in reversed(range(n)):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits