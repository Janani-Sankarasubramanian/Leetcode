# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #move currentNode n steps into list
        currentNode = head
        
        for i in range(n):
            currentNode = currentNode.next
        
        if currentNode is None: 
            return head.next
        
        #move both pointers until currentNode reaches end of list
        nodeBeforeRemoved = head
        
        while (currentNode.next != None):
            currentNode = currentNode.next
            nodeBeforeRemoved = nodeBeforeRemoved.next
        
        nodeBeforeRemoved.next = nodeBeforeRemoved.next.next
        
        return head
        
        