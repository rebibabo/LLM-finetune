class Solution:
    
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        p, i = dummy, 0
        while i < n:
            p = p.next
            i += 1
        l = dummy
        while p.next:
            p = p.next
            l = l.next
        l.next = l.next.next if l.next else None
        return dummy.next