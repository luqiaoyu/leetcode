package lc8;

/**
 * Created by luqiaoyu on 2018/11/8.
 * 8. String to Integer (atoi)
 * 24ms 73.33%
 */
public class Solution {
    public int myAtoi(String str) {
        int n = str.length();
        if (n == 0) return 0;

        int res = 0;
        boolean flag = false;
        boolean sign = false;
        for (char x : str.toCharArray()) {
            if (! flag) {
                if (x == ' ') continue;
                if (x == '-') {
                    flag = true;
                    sign = false;
                    continue;
                }
                if (x == '+') {
                    flag = true;
                    sign = true;
                    continue;
                }
                int temp = x - '0';
                if (temp >= 0 && temp <= 9) {
                    flag = true;
                    sign = true;
                    res = res * 10 + temp;
                }
                else return 0;
            }
            else {
                int temp = x - '0';
                if (temp >= 0 && temp <= 9) {
                    if (sign) {
                        if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && temp > 7)) return Integer.MAX_VALUE;
                    }
                    else {
                        if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && temp > 8)) return Integer.MIN_VALUE;
                    }
                    res = res * 10 + temp;
                }
                else break;
            }
        }

        return sign ? res : -res;
    }
}
