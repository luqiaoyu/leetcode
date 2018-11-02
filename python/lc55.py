# 55. Jump Game

# bottom-up dynamic programming
# O(n^2)
# 64ms
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0: return False
        dp = [False for i in range(n)]    # 能否从index 0跳到index i
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):    # 要倒过来循环，否则会超时
                if (dp[j] and nums[j] >= i - j):
                    dp[i] = True
                    break
        return dp[n - 1]

# greedy
# O(n)
# 40ms faster than 100%
class Solution1:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0: return False
        target = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
