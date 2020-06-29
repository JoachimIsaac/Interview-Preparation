# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UMPIRE:

Understand: 
--> can we get an empty linked list? yes , if we do return None
--. what if we get a single node also we could jsut return it 
--> what do we return ? the linked list
--> do we have to do this inplace?
--> we have to move it from the right? yes


match:
--> Multi pass
--> get the length
--> do length % k to get how much we actually have to move
--> do length - remainder
==> if length mod k == 0 return 
Plan:

use remainder to iterate and then


1.check if empty or only one value

2. do a pass to get the length of the array 

3. get the value we need to traverse by doing k % length

4. try to iterate through the linked list again to get the posiiton we need to move the values length - k % length steps

5. move the numbers after curr to the front. 

length = 5

position = k % length = 2


length - position = 3

counter = 1 

counter += 1 

Input: head --->1---->2---->3---->4----->5----->NULL, k = 2
              curr   front
        head --> 5-->1---->2---->3---->4---->                        


get to position first

then do this 

#######to change the values
       
temp = front
curr.next = None


while front.next != None:
    front = front.next

front.next = head

head = temp

####################


length = 2

position = k % length = 0



# if position == 0:
    return head 
    
length - position = 2



1--->2-->None

head4---->5------>#1----->2---->3---->N   NULL, k = 2
                 curr            front
                            temp
 
counter = 3



length = 5

position = 2 % 5 = 2

distance = 5 - 2 = 3


"""


class Solution:
    def rotateRight(self, head, k):

        if head == None:
            return None

        if head.next == None:
            return head

        length = self.getLength(head)
        position = k % length

        if position == 0:
            return head

        distance = length - position

        curr = head
        front = head.next
        counter = 1

        while counter < distance:
            curr = curr.next
            front = front.next
            counter += 1

        temp = front
        curr.next = None

        while front.next != None:
            front = front.next

        front.next = head

        head = temp

        return head

    def getLength(self, head):
        counter = 1
        curr = head

        while curr.next != None:
            curr = curr.next
            counter += 1

        return counter
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode(-1)
        head2 = dummy
        carry = False
        
        while ptr1 != None or ptr2 != None:
            sum = 0 
            
            if ptr1 == None:
                sum += ptr2.val
                ptr2 = ptr2.next
                
            elif ptr2 == None:
                sum += ptr1.val
                ptr1 = ptr1.next
                
            else:
                sum += (ptr1.val + ptr2.val)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                
                
            if carry:
                sum += 1
                
            if sum >= 10:
                sum %= 10
                carry = True
            else:
                carry = False
                
            dummy.next = ListNode(sum)
            dummy = dummy.next
            
            if carry:
                dummy.next = ListNode(1)
            
        return head2.next
            