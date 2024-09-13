class Solution:
    
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0, head)
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        iter = length // k
        p = dummy
        for _ in range(iter):
            l, m, r = p.next, p.next.next, p.next.next.next if p.next.next else None
            for _ in range(k-1):
                m.next = l
                l, m, r = m, r, r.next if r else None
            p.next.next, p.next, p = m, l, p.next
        return dummy.next