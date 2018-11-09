package lc9;

/**
 * Created by luqiaoyu on 2018/11/9.
 * 9. Palindrome Number
 * Revert half of the number
 * aware of overflow
 * 78ms 100%
 */
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int rev = 0;
        while(x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }

        return x == rev || x == rev / 10;
    }
}
