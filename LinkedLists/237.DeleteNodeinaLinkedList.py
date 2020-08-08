# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
UMPIRE:
--> can we get an empty linked list ?
--> the node we are given is the one we want to delete? 
--> what if we have the tail ==> we wont getg the tail 
--> what do not return 
--> use extra space?

Match:
--> multi pass
--> multi pointer
--> unreference 

9 ------> None
      \
             |

node.val = node.next.val
node.next = node.next.next
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # O(1) time O(1)  space
        node.val = node.next.val
        node.next = node.next.next


#         curr = node O(n) time and O(1) space
#         forward = node.next

#         while forward:
#             curr.val = forward.val
#             curr = curr.next
#             forward = forward.next

#         while node.next != curr:
#             node = node.next


#         node.next = None
