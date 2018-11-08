package lc58;

/**
 * Created by luqiaoyu on 2018/11/8.
 * 58. Length of Last Word
 * 2ms 100%
 */
public class Solution1 {
    public int lengthOfLastWord(String s) {
        return s.trim().length()-s.trim().lastIndexOf(" ")-1;
    }
}
