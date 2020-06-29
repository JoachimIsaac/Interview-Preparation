"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

5 - 2 = 3
counter = 3


After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.


Follow up:
Could you do this in one pass?


UMPIRE:

Understand:
 --> can we assume that we will always have a valid n? (yes)
        --> can n be 0? seems it starts from 1 
        --> do we have to do this in place?
        ---> is the linekd list singlely or doublely linked?
---> multiple passes?

match: --> we need to track the length of the array to find where we need to delete.
--> 2 pointers
--> one pass
       --> so we need to get remainder by using length - n = the spot we need to actually start the delete process from 
--> counter 

Plan: 
1. we need to create a counter
2. we need to traverse through the linked list while length - n > our current counter
3. when we escape the linked list we need to attach curr.next to curr.next.next to remove the number at position (length - n + 1)

4. Then we return the head of the linked list.


evaluation :
--> time complexity ==> O(N) where N is the number of nodes in the linked list(input)
--> space complexity ==> O(1) constant since all we did was change the pointers of nodes we didn;t use extra space. 

wronngggg need to get better soltuion 
"""


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def printList(head):
    curr = head
    str1 = ""
    while curr != None:
        str1 += str(curr.val) + "-->"
        curr = curr.next

    print(str1)


dummy = Node(-1)
head = dummy

dummy2 = Node(-1)
head2 = dummy2

for index in range(1, 2 + 1):
    dummy2.next = Node(index)
    dummy2 = dummy2.next

for index in range(1, 5 + 1):
    dummy.next = Node(index)
    dummy = dummy.next


printList(head.next)
printList(head2.next)


class Solution:
    def removeNthNodeFromEndofList(self, head, N):

        if head.next == None and N == 1:
            return None

        counter = 1
        curr = head
        length = self.getLength(head)

        # if length == k:# what i found on btb if k == to the length
        #     curr = head.next
        #     head.next = None
        #     head = curr
        #     return head

        point_to_remove_from = length - N

        while (point_to_remove_from > counter):
            curr = curr.next
            counter += 1

        curr.next = curr.next.next

        return head

    def getLength(self, head):
        counter = 1
        curr = head
        while curr.next != None:
            counter += 1
            curr = curr.next

        return counter


s = Solution()
result1 = s.removeNthNodeFromEndofList(head.next, 2)
printList(result1)
result2 = s.removeNthNodeFromEndofList(head2.next, 2)
printList(result2)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

UMPIRE:

Understand:
--> What type of lnked list is being passed in?
--> Can we get an empty list?
--> Will n always be valid?
--> What if we get a list with a single node and we get n = 1

Match:
--> multi pass
--> two pointers
-->single pass
--> get the length 


Plan:

length = 
1---->2---->3---->4---->5, and n = 2.
           curr

position = 3 

get the length of the linked list 
then traverse while counter < position = length - n
then do rewiring 
and return head

can we do better ?

yes we can slightly

how? 

fast and slow pointers 





Plan: 

counter = 0
while counter <= n:

    


dummy--->----->2----->NOne, and n = 2 + 1
 s                        F

counter = 1


1. create fast and slow pointers 
2. loop the fast pointer counter <= n +1 time when counter = 0
3. move the slow pointer until fast == None
4. delete the node by doing slow.next = slow.next.next , this rewiring works because slow is at the number before the number we
want ot delete.
the dummmy node was key ...
dummy node prevent errors for cases where you are removing the head or even it cases where you only have like two values and you want to remove the head or the tail.


"""


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head == None:
#             return None
#         if head.next == None and n == 1:
#             return None
#         dummy = ListNode(-1)
#         dummy.next = head

#         fast = dummy
#         slow = dummy

#         counter = 1

#         while counter <= n+1:
#             fast = fast.next
#             counter += 1

#         while fast:
#             slow = slow.next
#             fast = fast.next

#         slow.next = slow.next.next

#         return dummy.next


# #         if head == None:
# #             return None
# #         if head.next == None and n == 1:
# #             return None


# #         length = self.get_length(head)

# #         position = length - n

# #         if position == 0:
# #             curr = head
# #             head = head.next
# #             curr.next = None
# #             return head

# #         curr = head
# #         counter = 1

# #         while counter < position:
# #             curr = curr.next
# #             counter += 1

# #         curr.next = curr.next.next

# #         return head


# #     def get_length(self,head):
# #         curr = head
# #         counter = 1

# #         while curr.next:
# #             curr = curr.next
# #             counter += 1

# #         return counter
