class Solution:
    
    def deleteDuplicates(self, head):
        dummy = ListNode(10e5, head)
        pre, l, r = dummy, head, head.next if head else None
        while r:
            if l.val == r.val:
                while r and l.val == r.val:
                    r = r.next
                pre.next = r
                l, r = r, r.next if r else None
            else:
                pre, l, r = l, r, r.next if r else None
        return dummy.next