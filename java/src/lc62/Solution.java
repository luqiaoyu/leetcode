package lc62;

/**
 * Created by luqiaoyu on 2018/12/7.
 * 62. Unique Paths
 * 0ms 100%
 */
public class Solution {
    public int uniquePaths(int m, int n) {
        int[] cur = new int[n];
        for (int i = 0; i < n; i++) {
            cur[i] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] += cur[j - 1];
            }
        }
        return cur[n - 1];
    }
}
