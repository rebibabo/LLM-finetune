class Solution:
    def partition(self, head, x: int):
        less, great, dummy = ListNode(0), ListNode(0), ListNode(0, head)    
        a, b = less, great  
        l, r = dummy, head  
        while r:
            l.next = None   
            if r.val < x:   
                a.next = a = r
            else:
                b.next = b = r
            l, r = r, r.next
        a.next = great.next    
        return less.next