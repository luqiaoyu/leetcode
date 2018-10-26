package lc69;

/**
 * Created by luqiaoyu on 2018/10/26.
 * 69. Sqrt(x)
 * binary search
 * 29ms
 */
public class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int left = 0;
        int right = x;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid == x / mid) {
                ans = mid;
                break;
            }
            else if (mid < x / mid) {
                left = mid + 1;
                ans = mid;
            }
            else {
                right = mid - 1;
            }
        }
        return ans;
    }
}
