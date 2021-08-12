# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        insert_node = TreeNode(val)

        if not root:
            return insert_node

        prev = None
        temp = root

        while temp is not None:
            if temp.val > val:
                prev = temp
                temp = temp.left

            elif temp.val < val:
                prev = temp
                temp = temp.right

        if prev.val > val:
            prev.left = insert_node
        else:
            prev.right = insert_node

        return root