# 69. Sqrt(x)

# binary search, 找到mid，使得mid * mid <= x < (mid + 1) * (mid + 1)
# 68ms
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x
        left = 0
        right = x
        while(left <= right):
            mid = left + (right - left) // 2
            if (mid == x // mid):
                ans = mid
                break
            elif (mid < x // mid):
                left = mid + 1
                ans = mid    # !!!
            else:
                right = mid - 1
        return ans


# Newton's method
# 72ms
class Solution1:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x // r) // 2
        return r