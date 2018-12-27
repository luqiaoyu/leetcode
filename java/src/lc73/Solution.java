package lc73;

/**
 * Created by luqiaoyu on 2018/12/27.
 * 73. Set Matrix Zeroes
 * time O(mn)
 * space O(1)
 * 2ms 48.89%
 */
public class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean first_row = false, first_col = false;

        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) first_row = true;
        }
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) first_col = true;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < n; j++) matrix[i][j] = 0;
            }
        }
        for (int j = 1; j < n; j++) {
            if (matrix[0][j] == 0) {
                for (int i = 1; i < m; i++) matrix[i][j] = 0;
            }
        }

        if (first_row) {
            for (int j = 0; j < n; j++) matrix[0][j] = 0;
        }
        if (first_col) {
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
        }
    }
}
