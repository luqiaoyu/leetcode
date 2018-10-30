package lc52;

/**
 * Created by luqiaoyu on 2018/10/29.
 * 52. N-Queens II
 * 4ms
 */
public class Solution {
    private int result = 0;
    public int totalNQueens(int n) {
        result = 0;
        int[] temp = new int[n];
        backtrack(0, n, temp);
        return result;
    }

    private void backtrack(int row, int n, int[] temp) {
        if (row == n) {
            result += 1;
        }
        else {
            for (int col = 0; col < n; col++) {
                temp[row] = col;
                if (isValid(row, n, temp)) {
                    backtrack(row + 1, n, temp);
                }
            }
        }
    }

    private boolean isValid(int row, int n, int[] temp) {
        for (int j = 0; j < row; j++) {
            if (temp[j] == temp[row] || temp[j] - j == temp[row] - row || temp[j] + j == temp[row] + row) return false;
        }
        return true;
    }
}
