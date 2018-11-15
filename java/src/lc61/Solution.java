package lc61;

/**
 * Created by luqiaoyu on 2018/11/15.
 * 61. Rotate List
 * 7ms 100%
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        ListNode p = head;
        int length = 1;
        while (p.next != null) {
            p = p.next;
            length++;
        }

        int k_mod = k % length;

        if (k_mod == 0)
            return head;
        else {
            int m = length - k_mod;
            ListNode q = head;
            for (int i = 0; i < m - 1; i++) {
                q = q.next;
            }
            ListNode res = q.next;
            q.next = null;
            p.next = head;
            return res;
        }
    }
}
