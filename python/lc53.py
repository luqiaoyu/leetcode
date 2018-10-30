# 53. Maximum Subarray

# DP: dp[i] means maximum subarray ending with nums[i]
# 48ms
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n == 0): return 0
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        result = max(dp)
        return result
        