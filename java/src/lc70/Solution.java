package lc70;

/**
 * Created by luqiaoyu on 2018/12/24.
 * 70. Climbing Stairs
 * DP
 * 3ms 30.57%
 */
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        int pp = 1, p = 2, res = 0;
        for (int i = 2; i < n; i++) {
            res = p + pp;
            pp = p;
            p = res;
        }

        return res;
    }
}
