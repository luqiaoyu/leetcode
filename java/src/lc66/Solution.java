package lc66;

/**
 * Created by luqiaoyu on 2018/12/20.
 * 66. Plus One
 * 0ms 100%
 */
public class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i] += 1;
                return digits;
            }
            else {
                digits[i] = 0;
            }
        }

        int[] res = new int[n + 1];
        res[0] = 1;
        return res;
    }
}
