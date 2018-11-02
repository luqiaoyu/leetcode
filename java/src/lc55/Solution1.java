package lc55;

/**
 * Created by luqiaoyu on 2018/11/2.
 * 55. Jump Game
 * greedy
 * O(n)
 * 4ms
 */
public class Solution1 {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        if (n == 0) return false;
        int target = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (i + nums[i] >= target) target = i;
        }
        return target == 0;
    }
}
