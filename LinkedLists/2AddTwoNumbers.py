# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
UMPIRE:

Understand:
--> we can't get an empty linked list for either of them 
--> they are in reversed order
--> we have to account for the fact that , one list can be shorter than another


1. set two pointers, one for each input list. create dummy node and new list head
2. add values that our pointers are at 
3. check if there 's a carry , add 1
4. check if sum >= 10 if it is, mod it and set carry flag = true 
5. Move pointers forward 
6. after loop, check if carry is true. if it is , add additional node to result list 
7. return result list'
"""


class Solution:
    def addTwoNumbers(self, l1, l2):

        # Create two pointers to each linked list of numbers
        ptr1 = l1
        ptr2 = l2

        # Create a dummy node
        dummy = ListNode(-1)

        # and a pointer to it
        head2 = dummy

        # declare a flag for the carry.
        carry = False

        # our loop needs to be or because one linked list could have a longer length than the other
        # in essence we could be adding a a world which is smaller and takes up less space in terms of units.
        while ptr1 != None or ptr2 != None:

            # declare a sum variable
            sum = 0

            # if we have finished traversing ptr1 but still have values in ptr2
            if ptr1 == None:
                # take the sum of the valid pointer
                sum += ptr2.val
                ptr2 = ptr2.next

            # if we have finished traversing ptr2 but still have values in ptr1
            elif ptr2 == None:
                # take the sum of the valid pointer
                sum += ptr1.val
                ptr1 = ptr1.next

            # we have both valid values in both ptr1 and ptr2 , both are not at None position
            else:
                # sum up both pointer's values and then advance them
                sum += (ptr1.val + ptr2.val)
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            # If the carry == True we add one to the sum
            if carry:
                sum += 1

            # If the sum is greater than or equal to 10
            if sum >= 10:
                # take the digit at the end
                sum %= 10
                # make carry equal True
                carry = True
            else:  # if sum is less make carry = False
                carry = False

            # add the new node and create it with our sum
            dummy.next = ListNode(sum)
            dummy = dummy.next

            # if we have a carry create node with 1 but we don't move the dummy pointer, that way if we need to add a new number over it
            # it still works .
            if carry:
                dummy.next = ListNode(1)

        return head2.next
