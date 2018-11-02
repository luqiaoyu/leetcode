package lc55;

/**
 * Created by luqiaoyu on 2018/11/2.
 * 55. Jump Game
 * dynamic programming
 * O(n^2)
 * 9ms
 */
public class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        if (n == 0) return false;
        boolean[] dp = new boolean[n];
        dp[0] = true;
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {    // 正序循环390ms，倒序循环9ms
                if (dp[j] && nums[j] >= i - j) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n - 1];
    }
}
