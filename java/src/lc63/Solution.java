package lc63;

/**
 * Created by luqiaoyu on 2018/12/7.
 * 63. Unique Paths II
 * 1ms 44.97% O(m * n)
 */
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;    // num of rows
        int n = obstacleGrid[0].length; // num of columns
        int[][] d = new int[m][n];
        if (obstacleGrid[0][0] == 1) return 0;
        else d[0][0] = 1;
        for (int i = 1; i < m; i++) {
            d[i][0] = obstacleGrid[i][0] == 1 ? 0 : d[i - 1][0];
        }
        for (int j = 1; j < n; j++) {
            d[0][j] = obstacleGrid[0][j] == 1 ? 0 : d[0][j - 1];
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                d[i][j] = obstacleGrid[i][j] == 1 ? 0 : d[i - 1][j] + d[i][j - 1];
            }
        }
        return d[m - 1][n - 1];
    }
}
