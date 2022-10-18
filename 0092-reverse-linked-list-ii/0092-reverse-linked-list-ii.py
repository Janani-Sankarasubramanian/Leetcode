# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        m, n = head, head
        stop = False
        def recurseandReverse(n, left, right):
            nonlocal m, stop
            
            if right == 1:
                return
            
            n = n.next
            
            if left > 1:
                m = m.next
            
            recurseandReverse(n, left-1, right -1)
            
            if m == n or n.next == m:
                stop = True
            
            if not stop:
                m.val, n.val = n.val, m.val
                m = m.next
        
        recurseandReverse(n, left, right)
        return head
        
        
        
        