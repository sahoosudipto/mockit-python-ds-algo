# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def Depth(root):
        #     if root == None:
        #         return 0
        #     else:
        #         return max(Depth(root.left), Depth(root.right)) + 1
        # if root != None:
        #     return Depth(root)
        # else:
        #     return 0
        # m = 0
        # s = [(root, 1)]
        # while s:
        #     (n, d) = s.pop()
        #     if n == None:
        #         continue
        #     m = max(d, m)
        #     s.append((n.left, d+1))
        #     s.append((n.right, d+1))
        # return m
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
        
