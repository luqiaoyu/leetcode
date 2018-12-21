package lc67;

/**
 * Created by luqiaoyu on 2018/12/21.
 * 67. Add Binary
 * 2ms 97.01%
 */
public class Solution1 {
    public String addBinary(String a, String b) {
        StringBuffer res = new StringBuffer();

        int c = 0, i = a.length() - 1, j = b.length() - 1;
        while (i >= 0 || j >= 0 || c == 1) {
            c += (i >= 0 ? a.charAt(i--) - '0' : 0);    // 加括号能提高运行速度
            c += (j >= 0 ? b.charAt(j--) - '0' : 0);
            res.append(c % 2);
            c /= 2;
        }
        return res.reverse().toString();
    }
}
