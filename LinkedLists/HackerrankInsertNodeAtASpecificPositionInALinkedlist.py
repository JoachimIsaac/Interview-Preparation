"""
Insert a node at a specific position in a linked list

You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

As an example, if your list starts as  and you want to insert a node at position  with , your new list should be 

Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:

head: a SinglyLinkedListNode pointer to the head of the list
data: an integer value to insert as data in your new node
position: an integer position to insert the new node, zero based indexing
Input Format

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer  denoting the data of the node that is to be inserted.
The last line contains an integer .

Constraints

, where  is the  element of the linked list.
.
Output Format

Return a reference to the list head. Locked code prints the list for you.

Sample Input

3
16
13
7
1
2
Sample Output

16 13 1 7
Explanation

The initial linked list is 16 13 7. We have to insert  at the position  which currently has  in it. The updated linked list will be 16 13 1 7

"""
#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
"""
UMPIRE:

Understand: 
--> can we get an empty list? yes add it to the head.
--> where do we add? we add at that specific position
--> is this a singlely linked list ?
--> what do we return?
--> can we use extra space?
--> do we return the list in place?

match: -->POINTERS, rearrange
       -->iterate through


plan: 

1. first we have to do a check for an empty list

if head == None and position == 0:
    head = SinglyLinkedListNode(value)

2. then we need to create a traversal loop that goes through the list looking for the correct index to stop at to make the change.

3. then return the head 



"""


def insertNodeAtPosition(head, data, position):

    if head == None and position == 0:
        head = SinglyLinkedListNode(data)
    else:

        curr = head
        counter = 1

        while counter < position:  # 16.  13  7. . insert 1
            curr = curr.next
            counter += 1
            print(curr.data)

        if curr.next != None:
            node = SinglyLinkedListNode(data)

            temp = curr.next
            curr.next = node
            node.next = temp
        else:
            curr.next = SinglyLinkedListNode(data)

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
