"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UMPIRE:

Understand:
--> What type of linked list are we getting ? (singlely lnked list )
--> Can we use extra space ? (yes)
--> What is our input and output? (True or false)
--> What is a palindrome? well a word that spells the same way backwards
--> what if we get an empty linked list or we get a linked list with one value? (just return true)


Match: pointers
       array
       single pass or multiple pass?


       Plan: traverse the linked list each time get each value and append it to an array.
             create a ispalindrome function and then check if it is

       this would be in the time complexit of O(n) and the space complexity of O(n)



Interviewer: This is good, but can we do better ?

Me: There is a possiblity we can optimize this by using less space.


Match:
--> Fast and slow pointer
--> Reverse a linked list


Plan:
reminder: account for the case of an empty linked list and a linked list with one node
head == None and head.next == None

1. Create fast and slow poitners
2. iterate throught the linked list where the fast moves(.next.next) and the slow pointer moves(.next) one behind the fast.
3. When fast approaches None(i.e while fast.next.next != None) we iterate through the list.
4. Fast will remain onthe part of the list we have to start reversing from .
5  reverse that part of the list
6. then set our slow and fast pointers to the new heads
7. traverse thorugh both and compare the values
8. if the values are diffrent return False
9. if we never return false return True



fast = head
slow = head


while fast.next.next != None:
    fast = fast.next.next
    slow = slow.next

fast = reverseList(fast) # return head

slow = head


while fast != None and slow != None:
    if fast.val != slow.val:
        return False

    slow = slow.next
    fast = fast.next

return True









"""


class Solution:


"""
Time complexity: O(n)
"""

   def isPalindrome(self, head):
        if head == None:
            return True

        if head.next == None:
            return True

        fast = head
        slow = head

        while fast.next and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        secondHalf = self.reverseList(slow.next)
        firstHalf = head

        while firstHalf != None and secondHalf != None:
            if firstHalf.val != secondHalf.val:
                return False

            secondHalf = secondHalf.next
            firstHalf = firstHalf.next

        return True

    def reverseList(self, head):

        curr = head
        last = None

        while curr != None:
            temp = curr.next
            curr.next = last
            last = curr
            curr = temp

        head = last

        return last


#     def isPalindrome(self, head: ListNode) -> bool:

#         if head == None: #handles empty case
#             return True

#         if head.next == None: #handles a case where we only have one character
#             return True


#         word = []
#         curr = head

#         while curr  != None: #O(n) where n is the number of nodes in the linked list
#             word.append(curr.val)
#             curr = curr.next


#         return self.arrIsPalindrome(word) #overall our time complexity is O(n) and the space is O(n)


#     def arrIsPalindrome(self,arr):#O(n) where n is the number of nodes in the linked list
#         left = 0
#         right = len(arr) - 1

#         while left < right:
#             if arr[left] != arr[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1

#         return True
