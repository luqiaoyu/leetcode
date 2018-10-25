# 50. Pow(x, n)

# recursive
# x^n = x^(n/2) * x^(n/2) * x^(n%2)
# 60ms
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: 
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        else:
            v = self.myPow(x, n // 2)
            if n % 2 == 0: 
                return v * v
            else:
                return v * v * x