# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        nums = nums[:left-1] + list(reversed(nums[(left-1):right])) + nums[right:]
        curr = head
        for num in nums:
            curr.val = num
            curr = curr.next
        return head
    
        
        