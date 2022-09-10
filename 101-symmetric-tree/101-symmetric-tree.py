# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        que.append((root, root))
        while que:
            levelSize = len(que)
            for _ in range(levelSize):
                (left, right) = que.popleft()
                if not left and not right:
                    continue
                elif None in [left, right]:
                    return False
                else:
                    if left.val != right.val:
                        return False
                    que.append((left.left, right.right))
                    que.append((left.right, right.left))
        return True