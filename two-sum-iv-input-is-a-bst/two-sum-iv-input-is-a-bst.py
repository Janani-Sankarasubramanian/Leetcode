# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __findTargetDetail(self, root, k, seen):
        if root is None:
            return False
        complement = k - root.val
        if complement in seen:
            return True
        else:
            seen.add(root.val)
        return self.__findTargetDetail(root.left, k, seen) or self.__findTargetDetail(root.right, k, seen)
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        return self.__findTargetDetail(root, k, seen)