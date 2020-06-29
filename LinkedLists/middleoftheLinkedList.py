"""
Problem Statement #
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3
Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
Example 3:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4


UMPIRE:

Understand: 
--> What type of linked list are we going to get ? Doubly or singley
--> can we get a empty linked list? yes
--> if we get a single node, what do we return , the node itself/
--> do we have to return the node that is at the middle position or the position of the node via indexing? the node itself

Match:
--> Two pointer 
--> double pass
--> getlength
--> iterating


Plan:
1. First we need to check if the linked list is empty or if it only has one value.
2. Then we need to loop through the linked list to get it's length
3. After checking if the length is odd or even we proceed accordingly.
4. if odd we take the ceil(length/2) and then we use a counter = 1 to find the middle
5. if it is even then we need to do (length/2) + 1, counter = 1 and counter has to get to 4



eval:

#O(n + m) wher n is the number of nodes in the linkedlist and m is the length/2 + 1 (generally half the length) 
and O(1) space



can we do better ? 


yes we can ....

if we can do it in one pass we can improve the time complexity

Plan:

what if we use two pointers, with one pointer moving twice as fast?


and what about odd vs even numbers ....


if fast == None :
    then it is odd

if fast.next == None:
     then it is even:


odd:
1 -> 2 -> 3 -> 4 -> 5 ->6--->7 null
               s                     f


even:
1 --> 2 --> 3 --> 4 --> 5 -->6-->null
                  s          f

so what do we do 

we set slow and fast to their start ing positions
slow = head
fast = head.next

and then we let them race 

while fast is not None or fast.next is not None:
    fast = fast.next.next
    slow = slow.next

if fast == None:
    return slow
else:
    return slow.next


O(n) time and O(1) space
n is the number of nodes in the linked list.

"""
import math


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    if head == None:
        return None

    if head.next == None:
        return head

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    if fast == None:
        return slow
    else:
        return slow.next


# def find_middle_of_linked_list(head):
#     if head == None:
#         return None

#     if head.next == None:
#         return head

#     curr = head
#     length = get_length(head)

#     if length % 2 == 0:  # Input: 1 -> 2 -> 3 -> 4 -> 5  -> null
#         length = (length / 2) + 1
#         return findNode(curr, length)
#     else:
#         length = math.ceil(length / 2)
#         return findNode(curr, length)


# def findNode(curr, length):
#     counter = 1
#     while counter < length:
#         curr = curr.next
#         counter += 1
#     return curr


# def get_length(head):
#     curr = head
#     counter = 1

#     while curr.next != None:
#         curr = curr.next
#         counter += 1

#     return counter


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
