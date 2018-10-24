package lc49;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/10/24.
 * 49. Group Anagrams
 * Categorize by sorted string: 18ms
 */
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList<>();
        Map<String, List> m = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if (!m.containsKey(key)) m.put(key, new ArrayList());
            m.get(key).add(s);
        }
        return new ArrayList(m.values());
    }
}
