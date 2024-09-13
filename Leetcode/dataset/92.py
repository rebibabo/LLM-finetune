class Solution:
    def reverseBetween(self, head, left: int, right: int):
        
        if not head.next or left == right:
            return head
        dummy = ListNode(0, head)   
        i, l, m, r = 1, dummy, dummy.next, dummy.next.next
        while i < left:
            l, m, r = m, r, r.next
            i += 1
        p = l
        while i <= right:
            m.next = l
            l, m, r = m, r, r.next if r else None
            i += 1
        p.next.next = m
        p.next = l
        return dummy.next