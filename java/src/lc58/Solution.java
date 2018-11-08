package lc58;

/**
 * Created by luqiaoyu on 2018/11/8.
 * 58. Length of Last Word
 * 5ms 40.28%
 */
public class Solution {
    public int lengthOfLastWord(String s) {
        int n = s.length();
        if (n == 0) return 0;

        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (res == 0) {
                if (s.charAt(i) == ' ') continue;
                else res++;
            }
            else {
                if (s.charAt(i) == ' ') break;
                else res++;
            }
        }

        return res;
    }
}
