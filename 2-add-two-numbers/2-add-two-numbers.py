# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        sentinel = ListNode(0)
        d = sentinel
        t_sum = 0;
        while (c1 != None or c2 != None):
            t_sum = t_sum//10
            if (c1 != None):
                t_sum += c1.val
                c1 = c1.next
                
            if (c2 != None):
                t_sum += c2.val
                c2 = c2.next
    
            d.next = ListNode(t_sum % 10)
            d = d.next

        if (t_sum // 10 == 1):
            d.next = ListNode(1)
            
        return sentinel.next