# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
UMPIRE:


--> we are getting a singlely linked list 
--> the calue x is asusumed to always be there 
--> what if we get an empty linked list (just return it ) same with one with only 1 value
--> keep the original order of the numbers 

Input: head = 1------>4------>3----->2----->5----->2, x = 3
              c
              
              
half less than and half greater than:

half less than: dummy---->1-->2-->2
half greater than or equal to: dummy--->4-->3--->5--->
Output: 1->2->2->4->3->5

attach the less than to the greater than
dummy.next = half greater than or equal to

result after fusion: dummy---->1-->2-->2--->4-->3--->5--->None


1-->2-->None n = 2

dummy--> 1
dummy-->2


head --> none :
return none 



match:
--> dummy node 
--> multi pass
--> out of place / inplace
--> use references 
--> 
"""


class Solution:
    def partition(self, head, x):  # Time O(n) and O(1) space

        if head == None:
            return None

        if head.next == None:
            return head

        lessThan = dummy1 = ListNode(-1)
        greaterOrEq = dummy2 = ListNode(-1)
        """
        Input: head = 1------>4------>3----->2----->5----->2, x = 3
                                                           c
        
        
        dummy1-->1-->2-->2--->None
        dummy2-->4-->3-->5--->None
        """

        curr = head

        while curr:
            if curr.val < x:
                dummy1.next = curr
                dummy1 = dummy1.next
                curr = curr.next
            else:
                dummy2.next = curr
                dummy2 = dummy2.next
                curr = curr.next

        # make sure the end of the greater than or equal to list ends with null.
        dummy2.next = None

        dummy1.next = greaterOrEq.next  # connect each of them

        return lessThan.next
