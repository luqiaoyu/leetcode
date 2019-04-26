package lc77;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by luqiaoyu on 2019/4/26.
 * 77. Combination
 * 16ms 73.16%
 */
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        dfs(1, k, temp, n, k, res);
        return res;
    }

    private void dfs(int cur, int left, List<Integer> temp, int n, int k, List<List<Integer>> res) {
        if (left < 0) return;

        if (left == 0) res.add(new ArrayList<>(temp));

        for (int i = cur; i < n + 1; i++) {
            temp.add(i);
            dfs(i + 1, left - 1, temp, n, k, res);
            temp.remove(temp.size() - 1);
        }
    }
}
