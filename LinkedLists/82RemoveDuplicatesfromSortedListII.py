"""
82. Remove Duplicates from Sorted List II
Medium


Share
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

UMPIRE: 
ordered hash table value:obj pair 
Understand:--> What type of linked list are we using?(doubly linked list or is it singlely linked)
           --> Do we have to get our solution in place, can we use extra space to help? 
           --> Will the values be in sorted order?(yes)
           --> oh so we need to 

Match: --> hash table
       --> iterate , multi
       --> rearrange poitners instead of creating a new linked list
       
PLan: 1. Use hash table to count how man occurances of a number there are in the linked list 
      2. After check if there is only one occurance and if there is create a node for the new linked list with that value
      3. iterate through the has table and keep doing that.
      4. then return the new linked list.
      
      



      dummy->1---->1---->1---->2---->3
                        currn       curr 
                             prev

"""




from sortedcontainers import SortedDict
class Solution:
    def deleteDuplicates(self, head):  # I need to understand the optimal solution
        if head == None:
            return None

        if head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy

        while prev.next:
            curr = prev.next

            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if curr != prev.next:
                prev.next = curr.next

            else:
                prev = curr

        return dummy.next


#     def deleteDuplicates(self, head): O(n)T , O(n)S
#         if head == None:
#             return None

#         if head.next == None:
#             return head

#         hash = SortedDict()

#         curr = head

#         while curr != None:
#             if curr.val not in hash:
#                 hash[curr.val] = 1
#             else:
#                 hash[curr.val] += 1

#             curr = curr.next

#         curr = head

#         dummy = ListNode(-1)
#         head2 =  dummy

#         for number in hash:
#             if hash[number] == 1:
#                 dummy.next = ListNode(number)
#                 dummy = dummy.next

#         if curr == None:
#             dummy.next = None


#         return head2.next
