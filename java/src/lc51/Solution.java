package lc51;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/10/29.
 * 51. N-Queens
 * 7ms
 */
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] temp = new int[n];
        backtrack(0, n, result, temp);
        return result;
    }

    private void backtrack(int row, int n, List<List<String>> result, int[] temp) {
        if (row == n) {
            List<String> sol = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < n; j++) {
                    if (j == temp[i]) sb.append('Q');
                    else sb.append('.');
                }
                sol.add(sb.toString());
            }
            result.add(sol);
        }
        else {
            for (int col = 0; col < n; col++) {
                temp[row] = col;
                if (isValid(row, n, temp)) {
                    backtrack(row + 1, n, result, temp);
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
