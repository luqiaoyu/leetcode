package lc59;

/**
 * Created by luqiaoyu on 2018/11/9.
 * 59. Spiral Matrix II
 * 2ms 43.62%
 */
public class Solution {
    public int[][] generateMatrix(int n) {
        if (n <= 0) return new int[0][0];

        int[][] res = new int[n][n];
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int r = 0, c = 0, di = 0;
        for (int i = 1; i < n * n + 1; i++) {
            res[r][c] = i;
            int cr = r + dr[di];
            int cc = c + dc[di];
            if (cr >= 0 && cr < n && cc >= 0 && cc < n && res[cr][cc] == 0) {
                r = cr;
                c = cc;
            }
            else {
                di = (di + 1) % 4;
                r = r + dr[di];
                c = c + dc[di];
            }
        }

        return res;
    }
}
