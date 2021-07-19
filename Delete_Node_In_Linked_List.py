# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Plan:
        1. Change the pointer of the given node
        2. Change the value of the given node
        """

        node.val = node.next.val
        node.next = node.next.next
