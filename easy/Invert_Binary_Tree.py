# Author:      Theodore Reyes
#
# Explanation: This algorithm works by simply swapping the left and right
#                   children of each node in the binary tree in a level-order/bfs fashion.
#
# Time:        O(n). Each node in the tree is enqueued/dequeued once, and has 
#              constant-time work performed
#
# Space:       O(n). At most, the queue will have ceil(n/2) nodes in it prior
#              to processing the leaves of the tree, if it is a full binary-tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I learned that Python Lists have O(n) removal from front, and was directed
# toward deque from collections
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Short circuit return if tree is empty
        if (root == None): return None

        # Enqueues root
        queue = deque()
        queue.append(root)

        # Performs level-order traversal, swapping each node's
        # left and right child nodes if they exist
        while (len(queue)):

            # Retrieve next node in queue
            node = queue.popleft()

            # Swap this node's children
            tmp = node.left
            node.left = node.right
            node.right = tmp

            # Enqueue child nodes (if they exist)
            if (node.left != None): queue.append(node.left)
            if (node.right != None): queue.append(node.right)

        return root

        
