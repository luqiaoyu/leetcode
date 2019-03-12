package lc2;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode cur = head;
        int c = 0;
        ListNode p1 = l1, p2 = l2;

        while (p1 != null || p2 != null || c != 0) {
            int op1 = (p1 == null) ? 0 : p1.val;
            int op2 = (p2 == null) ? 0 : p2.val;
            int s = op1 + op2 + c;
            c = s / 10;
            int v = s % 10;

            cur.next = new ListNode(v);
            cur = cur.next;

            if (p1 != null) p1 = p1.next;
            if (p2 != null) p2 = p2.next;
        }

        return head.next;
    }
}
