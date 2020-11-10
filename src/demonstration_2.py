"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    # Your code here
    # UPER

    # UNDERSTAND
    # 1) the first in the preorder is the root of the tree
    # 2) if i = index of the root in inorder, then everything to the left of i is the left subtree and everything right of i is the right subtree
    # How can we use ^^ to find the left/right subtrees in the preorder?

    # what do we need in order to be able to recurse?
    #   a base case
    #   subarrays -- inorder subarray and preorder subarray representing left/right subtrees

    # PLAN
    # 

