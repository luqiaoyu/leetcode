package lc60;

/**
 * Created by luqiaoyu on 2018/11/12.
 * 60. Permutation Sequence
 */
public class Solution {
    private int count = 0;
    private String res = '';

    public String getPermutation(int n, int k) {

    }

    private void backtrack(int n, int k, StringBuffer temp) {
        if (count == k) return;
        if (temp.length() == n) {
            count++;
            res = temp.toString();
            return;
        }

        for (int i = 1; i <= n; i++) {
            if temp.indexOf(i) continue;

        }
    }
}
