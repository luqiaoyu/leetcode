package lc71;

import java.util.*;

/**
 * Created by luqiaoyu on 2018/12/26.
 * 71. Simplify Path
 * 注：在Java中""和‘’是加以区分的，一个是String类型，一个是char类型
 * 22ms 28.92%
 */
public class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new LinkedList<>();
        for (String x : path.split("/")) {
            if (x.equals("") || x.equals(".")) continue;    // 一定要用.equals()!
            if (x.equals("..")) {
                if (!stack.isEmpty()) stack.pop();
                continue;
            }

            stack.push(x);
        }

        if (stack.isEmpty()) return "/";
        String res = "";
        for (String x : stack) {
            res = "/" + x + res;    // 似乎stack是倒过来取的
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String path = "/abc/...";
        String res = s.simplifyPath(path);
        System.out.println(res);
    }
}
