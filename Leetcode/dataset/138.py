class Solution:
    def copyRandomList(self, head):
        if not head:    
            return None
        map = {}    
        i, th = 0, head
        while th:
            map[hash(th)] = i
            i += 1
            th = th.next
        map[hash(None)] = -1    
        random_map = {}     
        i, th = 0, head
        while th:
            random_map[i] = map[hash(th.random)]
            th = th.next
            i += 1
        
        th = head
        copy_head = Node(head.val)
        copy_th = copy_head
        i, map = 1, {0: copy_th}
        th = th.next
        while th:       
            copy_th.next = Node(th.val)
            copy_th = copy_th.next
            map[i] = copy_th
            i += 1
            th = th.next
        
        i, th = 0, copy_head
        while th:       
            if random_map[i] == -1:
                th.random = None
            else:
                th.random = map[random_map[i]]
            th = th.next
            i += 1
        return copy_head