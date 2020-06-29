"""
Start of LinkedList Cycle (medium)

Problem Statement #
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
      def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()

"""
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.

UMPIRE: 
--> can we get and empty linked list ? yes
--> can we get a linked list of lenght 1? yes
--> we need to find the starting node of the cycle. can we assume we will always have cycle?
--> can we use extra space ?
--> is it a singlely linked list or a doubly linked list?


Match:
-->set/hash
-->fast and slow pointers?
--> iterate through

# what if the node behind where the two node meet is the cycle start node?
O(n)T O(n)S for the solution with set

O(n) T  and O(1)S for the solution with the fast and slow pointers.

let's attempt the solution with the set/hash

###

ok the solution with the hash worked....

but can we do better ?

yes we can...


Plan:

1. we need the length of the cycle
2. move the pointer2 k times = legnth of the cycle.
3. then keep moving pointer1 and pointer2 until they meet. ==> they will meet at the start
4. then we need to return the node that is the start of the linked list.

we pass throught many time but in the worst case we pass through big n times

simply we could say the time complexity is O(n)
but more psecifically we could say it is O(N + N + N) == O(3N) == O(N) <==(it simplifies down to)

space is O(1), we didn't use any extra space
"""
def find_cycle_start(head):
  if head == None:
    return "Invalid"
  
  if head.next == None:
    return "Invalid"

  slow = fast = find_cycle(head)

  length_of_cycle = get_length_of_cycle(slow)

  pointer1 = pointer2 = head

  counter = 0

  while counter < length_of_cycle:# move pointer 2 k steps k = to the length of the cycle.
    pointer2 = pointer2.next
    counter += 1

  while pointer1 != pointer2:
    pointer2 = pointer2.next
    pointer1 = pointer1.next

    if pointer1 == pointer2:
      return pointer2

  return pointer2




def get_length_of_cycle(meeting_point):
  slow = meeting_point.next
  fast = meeting_point
  counter = 1

  while slow != fast:
    slow = slow.next
    counter += 1
    if slow == fast:
      return counter

  return counter



def find_cycle(head):
  slow = head
  fast = head.next

  while slow != fast:
    fast = fast.next.next
    slow = slow.next

    if slow == fast:
      return slow

  return slow

#################################
# def find_cycle_start(head):
#   # TODO: Write your code here
#   if head == None:
#     return "Invalid"
  
#   if head.next == None:
#     return "Invalid"

#   set1 = set()

#   curr = head 

#   while curr != None:
#     if curr not in set1:
#       set1.add(curr)
#     else:
#       head = curr
#       return head

#     curr = curr.next

#   return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""

142. Linked List Cycle II
Medium

2590

207

Add to List

Share
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 
UMPIRE:

Understand: 
--> Can we have an empty linked list, a like list with only one node or a linked list with no cycle? (yes to all)
--> are we getting a singlely linked list? yes
--> do we have to return the indecx/ position of the start of the cycle? yes

Match:
--> two pointers (fast and slow)
--> multi-pass at worst O(N + N + ? ...)time and O(1) space if we just use pointers
--> counter varaibles
--> helper fucntions 
--> we need to catch easy signs of the linked list not having a cycle, will help with runtime, but not time complexity

Plan:


has_cycle(head):

    slow = head
    fast = nead.next
    
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    
    if fast == slow:
        return slow
            
    return False



get_cycle_length(head):
    fast = head
    slow = head.next
    counter = 1
    
    while slow != fast:
        slow = slow.next
        counter += 1
        
    return counter
    
   0 


detectCycle(head):
    if head == None:
        return -1
        
    if head.next = None:
        return -1
    
    meeting_point = hasCycle(head)
    
    if meetin_point == None:
        return -1
    else:
        cycle_length = get_cycle_length(meeting_point)
        
    counter = 0 
    
    pointer1 = pointer2 = head
    
    while counter < cycle_length:
        pointer1 = pointer1.next
        counter += 1
        
    index = 0
    
    while pointer1 != pointer2:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
        index += 1
        
    return index


time complexity: ==> O(3n) ==> O(n)
"""



# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if head == None:
#             return None
        
#         if head.next == None:
#             return None
        
        
#         meeting_point = self.has_cycle(head)
        
#         if meeting_point == False:
#             return None
#         else:
#             cycle_length = self.get_cycle_length(meeting_point)
        
#         counter = 0 
    
#         pointer1 = pointer2 = head
    
#         while counter < cycle_length:
#             pointer2 = pointer2.next
#             counter += 1
        
       
    
#         while pointer1 != pointer2:
#             pointer2 = pointer2.next
#             pointer1 = pointer1.next
            
        
#         return pointer1
    
    
    
    
    
    
    
    
    
    
#     def get_cycle_length(self,head):
#         fast = head
#         slow = head.next
#         counter = 1
    
#         while slow != fast:
#             slow = slow.next
#             counter += 1
        
#         return counter



        
#     def has_cycle(self,head):
        
#         slow = head
#         fast = head.next
        
#         while fast.next != None and fast.next.next != None:
#             fast = fast.next.next
#             slow = slow.next
        
#             if fast == slow:
#                 return slow
            
#         return False

        
        
        
        
        
