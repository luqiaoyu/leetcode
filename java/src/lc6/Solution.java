package lc6;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/11/5.
 * 6. ZigZag Conversion
 * Sort by Row
 * 30ms 83.07%
 */
public class Solution {
    public String convert(String s, int numRows) {
        int n = s.length();
        if (n <= numRows || numRows == 1) return s;

        List<StringBuilder> zigzag = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            zigzag.add(new StringBuilder());
        }

        int curRow = 0;
        boolean downFlag = false;
        for (char c: s.toCharArray()) {
            zigzag.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) {
                downFlag = ! downFlag;
            }
            curRow += downFlag ? 1 : -1;
        }

        StringBuilder res = new StringBuilder();
        for (StringBuilder row: zigzag) {
            res.append(row);
        }
        return res.toString();
    }
}
