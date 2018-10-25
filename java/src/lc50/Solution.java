package lc50;

/**
 * Created by luqiaoyu on 2018/10/25.
 * Pow(x, n)
 * 21ms
 */
public class Solution {
    public double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n > 0) return power(x, n);
        else {
            long m = -((long) n);       // 因为n的范围是int的最大范围，在取负的时候可能会overflow，所以要改变n的数据类型
            return power(1/x, m);
        }
    }

    private double power(double x, long n) {
        if (n == 0) return 1;       // 注意要有递归终止条件
        double v = power(x, n / 2);
        if (n % 2 == 0) return v * v;
        else return v * v * x;
    }
}
