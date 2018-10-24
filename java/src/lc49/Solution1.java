package lc49;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/10/24.
 * 49. Group Anagrams
 * Categorize by count
 * 36ms
 */
public class Solution1 {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList<>();
        Map<String, List> m = new HashMap<>();
        int[] count = new int[26];
        for (String s : strs) {
            Arrays.fill(count, 0);

            for (char c : s.toCharArray()) {
                count[c - 'a'] += 1;
            }

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                sb.append('#');
                sb.append(count[i]);
            }
            String key = sb.toString();
            if (!m.containsKey(key)) m.put(key, new ArrayList());
            m.get(key).add(s);
        }
        return new ArrayList(m.values());
    }
}
