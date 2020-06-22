"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UMPIRE:


Understand:

--->Should we do this in place or are we returning a new list ? yers we are returnning a new list!
---> can we assume that we will always get full lists? if we get an empty list what do we do?
    we can return the list that is not empty; if both are empty we return None.
--> does the new list have to be in order?
--> can we use extra space besides the space need to create the new list?


match: --> two pointers , exploring both liked lists 
       ---> decision making based on the value amounts
       --> one pass through each list?
       
       
Plan:

1. we need to do the checks for empty lists

2. we then need to create a loop that traverses through both lists and moves based on which number is less than another number
it should also always run as long as one of them doesn't equal none(the pointers).
3. when we leave the loop there may be a list that hasn't fully been traversed , we just connect the last node we were on within that list to our jointed list. 

4. after adding and making connections based on whether the node was less than or not we return the newly created list.



of course this would allow us to do this in a time complexity of O(n + m) where n is the number of nodes in the first list and m is the. number of nodes in the second list; and a space complexity of O(N) because we use  extra space than the space that will be used for our output.

WE CAN OPTIMIZE THIS BY JUST CONNECTING TO THE NODES IN PLACE IN STEAD OF MAKING NEW NODES



alternitively we could use and array to store all values use the same decision making methods to append to the array and then just load the linked list in that order. the issue with that is we would be using O(n + m) extra space.



INTERVIEWER:  can we do this recursively?

Me: ... yes we can 

Recursive Plan:

1. we need a basecase; the base case should be when one of the lists are empty
2. Then we need the bussiness logic that checks which is less and moves the pointers forward after deciding and adding a value. 
   The bussiness logic does this until we hit our base case.
3. After the base case is hit we add the rest of the list to our merged list and return the answer right away.

O(N + M) time and space 

"""


class Solution:
    def merge(self, L1, L2, curr, dummy):
        if L1 != None and L2 != None:
            if L1.val < L2.val:
                curr.next = L1
                curr = curr.next
                L1 = L1.next
            else:
                curr.next = L2
                curr = curr.next
                L2 = L2.next

        if L1 == None:
            curr.next = L2
            return dummy.next
        elif L2 == None:
            curr.next = L1
            return dummy.next

        return self.merge(L1, L2, curr, dummy)

    def mergeTwoLists(self, L1, L2):
        if L1 == None and L2 != None:
            return L2
        elif L2 == None and L1 != None:
            return L1
        elif L1 == None and L2 == None:
            return None

        dummy = ListNode(-1)
        curr = dummy

        return self.merge(L1, L2, curr, dummy)


#     def mergeTwoLists(self, L1, L2):#T O(M+N) , S O(1)
#         if L1 == None and L2 != None:
#             return L2
#         elif L2 == None and L1 != None:
#             return L1
#         elif L1 == None and L2 == None:
#             return None

#         dummy = ListNode(-1)
#         curr = dummy

#         while L1 != None and L2 != None:

#             if L1.val < L2.val:
#                 curr.next = L1
#                 curr = curr.next
#                 L1 = L1.next
#             else:
#                 curr.next = L2
#                 curr = curr.next
#                 L2 = L2.next


#         if L1 == None:
#             curr.next = L2
#         else:
#             curr.next = L1


#         return dummy.next

#     def mergeTwoLists(self, L1, L2):
#         if L1 == None and L2 != None:
#             return L2
#         elif L2 == None and L1 != None:
#             return L1
#         elif L1 == None and L2 == None:
#             return None

#         dummy = ListNode(-1)
#         curr = dummy

#         while L1 != None and L2 != None:

#             if L1.val < L2.val:
#                 curr.next = ListNode(L1.val)
#                 curr = curr.next
#                 L1 = L1.next
#             else:
#                 curr.next = ListNode(L2.val)
#                 curr = curr.next
#                 L2 = L2.next


#         if L1 == None:
#             curr.next = L2
#         else:
#             curr.next = L1


#         return dummy.next
