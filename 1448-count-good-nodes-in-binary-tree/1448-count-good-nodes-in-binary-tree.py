# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Start by creating a stack and append the root node and the max value to it, use a Tuple may be
        #Pop the last element out of the list and compare the max value and the root node
        #if the comparison is greater, increment the num of good nodes
        #Add the left and right children of the node to the stack, along with its max value so far
        #Iterate until the stack is empty and return the final num of good nodes
        
        stack = [(root, root.val)]
        
        num_good_nodes = 0
        
        while stack:
            node, max_so_far = stack.pop()
            
            if node.val >= max_so_far:
                num_good_nodes += 1
                max_so_far = node.val
            
            if node.left:
                stack.append((node.left, max_so_far))
            
            if node.right:
                stack.append((node.right, max_so_far))
        
        return num_good_nodes
                
            
        