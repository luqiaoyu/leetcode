# 61. Rotate List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 56ms
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (not head or not head.next or not k): 
            return head

        p = head
        n = 1
        while (p.next != None):
            n += 1
            p = p.next

        k_mod = k % n

        if k_mod == 0:
            return head
        else:
            m = n - k_mod
            q = head
            for _ in range(m - 1):
                q = q.next
            res = q.next
            q.next = None
            p.next = head
            return res

        
        