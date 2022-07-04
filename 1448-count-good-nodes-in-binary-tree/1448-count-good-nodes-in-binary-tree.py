# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Start a recursive function, initializing it from the root node
        #keep a max value and the number of good nodes stored
        #compare the node with the max value and update the number of good nodes if it is greater
        #if the left node is not none, recall the recursion function with left.
        #if the right node is not none, recall the recursion function with right.
        
        
        def countNodes(node, max_so_far):
            nonlocal num_good_nodes
            
            if node is None:
                return None
            
            if node.val >= max_so_far:
                num_good_nodes += 1
                   
            if node.right:
                countNodes(node.right, max(node.val, max_so_far))
     
            if node.left:
                countNodes(node.left, max(node.val, max_so_far))
        
        num_good_nodes = 0
        countNodes(root, float("-inf"))
        return num_good_nodes