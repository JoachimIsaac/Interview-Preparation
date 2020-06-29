"""

Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

"""
UMPIRE:

Understand:
--> Is the linked list singlely or doubly linked?
--> Can we get a linked list without a cycle, including empty list or a single Node? NO
--> What do we have to return? an integer?

Match:
--> fast and slow pointers
--> multiple passes
--> counter

Plan:
1. First I need to find the point at which the cycle the fast and slow pointers meet
2. then we need to take the slow pointer. next and make it iterate until it reaches the fast pointer again
3. we need to have a counter that start from 1


time  complexity ==> O(n)
space complexity ==> O(1)

"""


class Node:
      def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
  slow = head
  fast = head.next

  while fast != slow:
    fast = fast.next.next
    slow = slow.next
    if fast == None:
      return "Not a linked list with a cycle"

  return calculate_cycle_length(slow,fast)

def calculate_cycle_length(curr,fast):
    curr = curr.next
    counter = 1

    while curr != fast:
      curr = curr.next
      counter += 1

    return counter

  



















# def find_cycle_length(head):
#   slow, fast = head, head
#   while fast is not None and fast.next is not None:
#     fast = fast.next.next
#     slow = slow.next
#     if slow == fast:  # found the cycle
#       return calculate_cycle_length(slow)

#   return 0


# def calculate_cycle_length(slow):
#   current = slow
#   cycle_length = 0
#   while True:
#     current = current.next
#     cycle_length += 1
#     if current == slow:
#       break
#   return cycle_length




"""
