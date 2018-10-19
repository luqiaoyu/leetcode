package lc47;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/10/19.
 * 47. Permutations II
 */
// backtracking: 3ms
public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        boolean[] used = new boolean[nums.length];    // initialized as false
        backtrack(result, new ArrayList<>(), nums, used);
        return result;
    }

    private void backtrack(List<List<Integer>> result, ArrayList<Integer> tempList, int[] nums, boolean[] used) {
        if (tempList.size() == nums.length) {
            result.add(new ArrayList<>(tempList));
        }
        else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] == true || (i > 0 && nums[i] == nums[i - 1] && used[i - 1] == false)) continue;
                else {
                    used[i] = true;
                    tempList.add(nums[i]);
                    backtrack(result, tempList, nums, used);
                    used[i] = false;
                    tempList.remove(tempList.size() - 1);
                }
            }
        }
    }
}
