"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""

UMPIRE:


Understand:
--> what is a cycle?
--> What do we return to determine if the answer is correct? 
--> What if there is only one node => return 
--> what is the single node points to itself, is that a cycle?
--> can we use more space ? yes
--> is this a singlely linked list? (yes)
--> are there any duplicate number ?yes

Match:
--> pointers?
--> fast and slow?
--> hash tables/set?




plan: 

1.check if it is empty or if there is only one node 
2. make a hash/set 
3. traverse through the array until we hit null or we get a value we have already gotten.
4. if we get a value that is already in the hash return True
5. if we hit null return false 




time == > O(n) where n is the number of nodes + 1
space ==> O(n) Where n is the number of nodes + 1

Interviewer: can we do better ?

Me: yes i think we can buy optimizing our space usage.


plan : 
what if we have a fast and slow pointer and if they meet then it is a cycle if fast hits null it is not in a cycle




fast = head
slow = head


while fast.next != None and fast.next.next != None:
    if fast == slow:
        return True
    
    fast = fast.next.next
    slow = slow.next
    
return False
    

"""


class Solution:
    def hasCycle(self, head):  # Time O(n) ; space O(1)
        if head == None:
            return False

        if head.next == None:
            return False

        fast = head.next  # They have to start at different positions.
        slow = head  # cause we would not enter the while loop if they didn't.

        while slow != fast:

            if fast == None or fast.next == None:
                return False

            fast = fast.next.next
            slow = slow.next

        return True

    def hasCycle(self, head):  # Time O(n) ; space O(n)
        hash = set()
        curr = head
        while curr != None and curr.next != None:
            if curr not in hash:
                hash.add(curr)
            else:
                return True

            curr = curr.next

        return False
