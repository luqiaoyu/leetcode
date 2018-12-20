package lc64;

/**
 * 64. Minimum Path Sum
 * 7ms 35.24% O(m*n)
 */
public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[] dp = grid[0];

        for (int i = 1; i < n; i++) {
            dp[i] += dp[i - 1];
        }

        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j];
            }
        }

        return dp[n - 1];
    }
}
