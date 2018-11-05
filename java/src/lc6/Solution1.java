package lc6;

/**
 * Created by luqiaoyu on 2018/11/5.
 * 6. ZigZag Conversion
 * Visit by Row
 * 36ms 67.04%
 */
public class Solution1 {
    public String convert(String s, int numRows) {
        int n = s.length();
        if (n <= numRows || numRows == 1) return s;

        int cycleLen = 2 * (numRows - 1);
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                res.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n) {
                    res.append(s.charAt(j + cycleLen - i));
                }
            }
        }

        return res.toString();
    }
}
