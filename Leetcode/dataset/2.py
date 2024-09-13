class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        len1, len2 = 0, 0
        h1, h2 = l1, l2 
        while h1:   
            len1 += 1
            h1 = h1.next
        while h2:
            len2 += 1
            h2 = h2.next
        if len1 < len2:
            l1, l2 = l2, l1
        head = l1
        while l1:   
            sum = l1.val + l2.val + carry
            if sum >= 10:
                l1.val = sum % 10
                carry = 1
            else:
                l1.val = sum
                carry = 0
            if l2.next:
                l2 = l2.next
            else:        
                l2.val = 0
            if not l1.next and carry:   
                l1.next = ListNode(1, None)
                break
            l1 = l1.next
        return head