# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = list()

        self.recursive_post_travel(root, result)

        return result

    def recursive_post_travel(self, root, result):
        if root:
            self.recursive_post_travel(root.left, result)
            self.recursive_post_travel(root.right, result)
            result.append(root.val)