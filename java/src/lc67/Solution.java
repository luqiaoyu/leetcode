package lc67;

/**
 * Created by luqiaoyu on 2018/12/21.
 * 67. Add Binary
 * 3ms 52.58%
 */
public class Solution {
    public String addBinary(String a, String b) {
        String res = new String();

        int c = 0, i = a.length() - 1, j = b.length() - 1;
        while (i >= 0 || j >= 0 || c == 1) {
            c += (i >= 0 ? a.charAt(i--) - '0' : 0);
            c += (j >= 0 ? b.charAt(j--) - '0' : 0);
            res = Integer.toString(c % 2) + res;
            c /= 2;
        }
        return res;
    }
}
