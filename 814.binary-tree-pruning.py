#
# @lc app=leetcode id=814 lang=python
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def containsOne(node):
            if not node:
                return False
            
            # Recursively prune left and right subtrees
            left_contains_one = containsOne(node.left)
            right_contains_one = containsOne(node.right)
            
            # If left subtree does not contain 1, set it to None
            if not left_contains_one:
                node.left = None
            
            # If right subtree does not contain 1, set it to None
            if not right_contains_one:
                node.right = None
            
            # Return True if the current node or any of its subtrees contain 1
            return node.val == 1 or left_contains_one or right_contains_one
        return root if containsOne(root) else None
 
# @lc code=end

