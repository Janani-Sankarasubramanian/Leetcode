# Definition for a binary tree node.
from collections import deque 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Start by creating a queue and append the root node and the max value to it, use a Tuple may be
        #Pop the first element out of the list and compare the max value and the root node
        #if the comparison is greater, increment the num of good nodes
        #Add the left and right children of the node to the stack, along with its max value so far
        #Iterate until the stack is empty and return the final num of good nodes
                    
        queue = collections.deque([(root, float(-inf))])
        num_good_nodes = 0
        
        while queue:
            node, max_so_far = queue.popleft()
            
            if max_so_far <= node.val:
                num_good_nodes += 1
            
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
                
            if node.left:            
                queue.append((node.left, max(node.val, max_so_far)))
                
        return num_good_nodes