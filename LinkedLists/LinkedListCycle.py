"""
LinkedList Cycle (easy)

Problem Statement #
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

"""


class Node:
      def __init__(self, value, next=None):
    self.value = value
    self.next = next
"""
UMPIRE:
Understand: --> what type of linked list are we going to get in the input of our function?(singlely)
            --> Do we have to do this in place?
            --> can we assume that we can recieve and empty linkedlist as input or a single node?(yes)
            --> can a single node point back to itself? (no)
            
Match: --> Two pointer(fast and slow) ==> O(n) time , O(1) space
       --> Set/hash. ==> O(n) time , O(n) space
       --> iteration 
trade offs 


Plan: 1. check if the head is None or if we only have one Node (return False)
      2. Then we create a set and then we create a loop that iterates throughout the linked list
      3. while going through the linked list we need to add nodes that have not been already our set()
      4. if a node is already there then we return True, if not and we hit None we return False.


if head == None:
  return False

if head.next = None:
  return False


curr = head 
set1 = set()

while curr != None:
  if curr not in set1:
    set1.add(curr)
  else:
    return True

  curr = curr.next

return False 

O(n) Time 
O(n) Space

Can we do better ?

Yes we can:

for us to do better we would have to try using two pointers, one slow and one fast and if the 
fast one hits none then we know that it is not a cyclyic linked list

plan: 

1. We have to handle the empty and single cases 
2. Then we need create the pointers slow = head and fast = head.next
3. the we need a loop that let's the fast pointer iterate by two and the slow by one.




      s.                       f.
1---->2----->3---->4---->5---->6--->

                  s.f.
1---->2----->3---->4---->5---->6
              \               /
                \           /
                  \       /
                    \    /
                      \ /


slow = head
fast = head.next

while fast.next != None and fast.next.next != None:
  if fast == slow:
    return True 
  else:
    fast = fast.next.next
    slow = slow.next

return False

O(N) time 
O(1) Space
"""

def has_cycle(head):
  if head == None:
    return False

  if head.next == None:
    return False

  slow = head
  fast = head.next

  while fast.next != None and fast.next.next != None:
    if fast == slow:
      return True 
    else:
      fast = fast.next.next
      slow = slow.next
  return False


# def has_cycle2(head):
#   if head == None:
#     return False

#   if head.next == None:
#     return False


#   curr = head 
#   set1 = set()

#   while curr != None:
#     if curr not in set1:
#       set1.add(curr)
#     else:
#       return True

#     curr = curr.next
  
#   return False 


