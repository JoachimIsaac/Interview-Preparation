# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
UMPIRE:


Understand:
--> So we are going to recieve an array of linked lists as our input?yes
--> Can we use extra space?
--> What do we return ? a sorted linked list that has all the values 
--> what if the input is empty or it only has one list? return None or the list 


Match:
--> we can use a heap(sorted list class)
--> then we can loop over it and create a linked list like that 


Plan:
--> declare sortedcontainers class and import SortedList
--> iterate through the array and load all the values of each list into the array
--> create the list and then return it 



[
  1->4->5,
  
  1->3->4,
  
  2->6
]

[1,1,2,3,4,4,5,6]

Evaluate:

Time complexity: O(N * K) where N is the number of list and K is the number of values in each list
Space complexity O(K)

Still need to learn optimal solution with heap 
"""

from sortedcontainers import SortedList


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        numbers = SortedList([])

        for curr_list in lists:
            curr = curr_list

            while curr:
                numbers.add(curr.val)
                curr = curr.next

        dummy = ListNode(-1)
        result = dummy

        for number in numbers:
            dummy.next = ListNode(number)
            dummy = dummy.next

        return result.next
