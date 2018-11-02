package lc5;

/**
 * Created by luqiaoyu on 2018/11/1.
 * 5. Longest Palindromic Substring
 * expand around center
 * O(n^2)
 * 15ms
 */
public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = extendAroundCenter(s, i, i);
            int len2 = extendAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int extendAroundCenter(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left --;
            right ++;
        }
        return right - left - 1;
    }
}
