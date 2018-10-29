package lc3;

import java.util.HashMap;

/**
 * Created by luqiaoyu on 2018/10/29.
 * 3. Longest Substring Without Repeating Characters
 * 35ms
 */
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int i = 0, j = 0;
        HashMap<Character, Integer> d = new HashMap<>();
        int n = s.length();
        for (j = 0; j < n; j++) {
            if (!d.containsKey(s.charAt(j)) || d.get(s.charAt(j)) < i) {    // !!!
                d.put(s.charAt(j), j);
            }
            else {
                result = Math.max(result, j - i);
                i = d.get(s.charAt(j)) + 1;
                d.put(s.charAt(j), j);
            }
        }
        result = Math.max(result, j - i);    // !!!
        return result;
    }
}
