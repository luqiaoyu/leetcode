package lc53;

/**
 * Created by luqiaoyu on 2018/10/30.
 * 53. Maximum Subarray
 * DP: dp[i] means maximum subarray ending with nums[i]
 * 9ms
 */
public class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] dp = new int[n];
        dp[0] = nums[0];
        int result = dp[0];
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1] > 0 ? nums[i] + dp[i - 1] : nums[i];    // 三元条件比Math.max要快
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}
