package lc43;

/**
 * Created by luqiaoyu on 2018/10/16.
 * 43. Multiply Strings
 * 大数乘法
 */

// index i * index j --> index i + j, index i + j + 1: 17ms
public class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length();
        int n = num2.length();
        int[] pos = new int[m + n];
        // 一定是从右往左开始乘，并加起来
        for(int i = m - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                int temp = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int p1 = i + j;
                int p2 = i + j + 1;
                int sum = temp + pos[p2];

                pos[p2] = sum % 10;
                pos[p1] += sum / 10;
            }
        }

        StringBuilder sb = new StringBuilder();
        // 省略高位0
        for(int p: pos) if(!(sb.length() == 0 && p == 0)) sb.append(p);
        return sb.length() == 0 ? "0" : sb.toString();
    }
}

