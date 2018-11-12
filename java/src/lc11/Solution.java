package lc11;

/**
 * Created by luqiaoyu on 2018/11/12.
 * O(n)
 * 5ms 95.28%
 */
public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int area = 0;

        while (left < right) {
            int low = Math.min(height[left], height[right]);
            area = Math.max(area, (right - left) * low);

            if (height[left] < height[right]) {
                while (left <= right && height[left] <= low) {    // 注意顺序，否则运行时会报越界错误
                    left++;
                }
            }
            else {
                while (right >= left && height[right] <= low) {
                    right--;
                }
            }
        }

        return area;
    }
}
