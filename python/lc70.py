# 70. Climbing Stairs

# DP
# 考虑最后一步为1(dp[i - 1]) 或2(dp[i - 2])
# 52ms 23.91%
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# 48ms 29.05%
# 思路同上，只是减少空间复杂度
class Solution1:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        pp = 1
        p = 2
        for _ in range(3, n + 1):
            res = p + pp
            pp = p
            p = res

        return res
