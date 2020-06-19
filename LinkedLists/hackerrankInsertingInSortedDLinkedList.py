"""
Inserting a Node Into a Sorted Doubly Linked List

Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it into a sorted linked list while maintaining the sort.

Function Description

Complete the sortedInsert function in the editor below. It must return a reference to the head of your modified DoublyLinkedList.

sortedInsert has two parameters:

head: A reference to the head of a doubly-linked list of DoublyLinkedListNode objects.
data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

Input Format

The first line contains an integer , the number of test cases.

Each of the test case is in the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer, the data for each node of the linked list.
The last line contains an integer  which needs to be inserted into the sorted doubly-linked list.
Constraints

Output Format

Do not print anything to stdout. Your method must return a reference to the  of the same list that was passed to it as a parameter.

The ouput is handled by the code in the editor and is as follows:
For each test case, print the elements of the sorted doubly-linked list separated by spaces on a new line.

Sample Input

1
4
1
3
4
10
5
Sample Output

1 3 4 5 10
"""
#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


"""
UMPIRE: 

Understand: --> Is it a doubly or singlely linked list? (doublely linked list)
            --> What happens if a linked list is empty or only has one node? (it is still considered sorted)
            --> So when we get a value we just have to put it in place where it keeps the order?
            --> what do we return ? (we return a reference to the head node)
            --> do we have a constriant on space usuage ?(yes)
            --> what input do we have? (head, data)
            --> if head == None : head = NewNode(value)
            --> if currentNode.next == None , currentNode.next = newNode(value)
            
            def sortedInsert(head,data):
            
                eg
            data = 5
            <-1->3<->4<->5<->10<->NULL
            
            1<->3<->4<->5<->10<->NULL


match: --> One pass iteration
       --> Two pointer? or single pointer?
       --> I thing our best we can do inherently  on average or worst is O(n) space due to the nature of a linked list and what the question asks for.


Plan: 

def sortedInsert(head,data):
# If we have zero nodes:
  if head == None:
    head = DoublyLinkedListNode(data)
  else:
    current = head

    while current.next != None and current.next.data < data:
        current = current.next
    
    if current.next == None:
        current.next = DoublyLinkedListNode(data)
    else:
        temp = DoublyLinkedListNode(data)
        temp.prev = current
        temp.next = current.next
        current.next = temp

 return head
       

 special case , when the head is greater than our input. 

"""


def sortedInsert(head, data):
    if head == None:
        head = DoublyLinkedListNode(data)
    else:
        current = head

    while current.next != None and current.next.data < data:
        current = current.next

    if head.data > data:
        temp = DoublyLinkedListNode(data)
        temp.next = head
        head.prev = temp
        head = temp
        return head

    if current.next == None:
        temp = DoublyLinkedListNode(data)
        current.next = temp
        temp.prev = current
    else:
        temp = DoublyLinkedListNode(data)
        temp.prev = current
        temp.next = current.next
        current.next = temp

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
