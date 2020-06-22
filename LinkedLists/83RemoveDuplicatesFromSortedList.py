# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
UMPIRE:

UNDERSTAND: --> can we get an empty linked list? (yes) what do we return ? ==> None
            --> what if we get a linked list with only one value? just return it ?
            --> Do we have to do this inplace?
            --> can we do we have to do this in linear time?
            
            
            
           def deleteDuplicates(self, head: ListNode) -> ListNode: 
           
           Input: 1->1->2
           Output: 1->2
    
            Input: 1->1->2->3->3
            Output: 1->2->3
            
Match: --> linked list problem 
       --> two pointer approach 
       --> could use a hash table nut that would be more space
       -->  loop and rewire
       
       
Plan(hash): --> we do checks to see if we have a single value
            --> then after we loop through the array loading all the unique values into our set/hash
            --> then we loop though our has creating the new linked list using the unique values.
            
            

time complexity: O(N) and space complexity O(N) N is the number nodes in our linked list, why? because in the worst case we could have all unique characters. time complexity is just O(n) because we are using the Sortedset() which has a time complexity of O(log(n)) for adding values and it keeps the values in sorted order. Where as if we use a normal set we would have to sort it and our time complexity would move to bigO ( nlog(n))


Interviewer: Can you do better ?
Me: yeah, i think the way we can improve on the solution is to make sure we use less space, due to the nature of a linked list , we have to traverse the linked list to be able to get an answer. so we for sure will have a time complexity that at best will be linear.
We can improve by doing this inplace, essentially keeping our space use constant.



Plan: 1. first we need to check if we have an empty list or only one value
      2. then we need to create two pointers, which starts at the head and the other that start one place ahead.
      3. the second pointer should move until our first pointer's value is not equal to the second pointer.
         after doing that connections need to be made and the first pointer should move to the position of the second pointer.
      4. the loop should move while ptr1 and ptr2 donot qual none.
      5. then we should return our dummy node.
      
      Input: 1->1->2->3->3
                             pt1 ptr2
      
        Output: 1->2->3
        
        -->start at first and second
        -->ask if the pointers are equal if they are move ptr2
        ---> if they are different, connect pointer1.next to ptr2.
        --> when connected, make ptr1 = ptr2 and then increment ptr2
        --> if ptr2 == None or != ptr2 make ptr1 point to ptr2
        --> then return dummy.next
        
        
        if head == None:
            return None
        
        if head.next == None: 
            return head
            
        dummy = ListNode(-1)
        
        head2 = dummy


        ptr1 = head
        ptr2 = head.next
        
        dummmy.next = ptr1
        dummy = dummy.next
        
        while ptr1 != None and ptr2 != None:
            if ptr1.val == ptr2.val:
                ptr2 = ptr2.next
            else:
                dummy.next = ptr2
                dummy = dummy.next
                ptr1 = ptr2
                ptr2 = ptr2.next
                
        if ptr2 == None:
            dummy.next = None
            
        return head2.next
        
         Input: 1->1->2->3->3
        Output: 1->2->3
                
                
                
      1->  1-> 2->  3->  3->
                   ptr1     ptr2

dummy-->1->2->3->None
            dummy
            
            
            
Interviewer: can we do this with less code? let's just assume that there will be at most 1 extra copy of a number.
me: yes I think we can simplify the code.



let's assume that there is atmost 1 duplicate of a number if there is a duplicate, assuming this current.next.next plays a big role in our logic


Plan: we would have to use two pointers or inactuality we could just use one and build the list withh refeerences. 
     --> our current node will start at the head and we will keep checking whether current.next == None or if current.next.next == None
     --> After that we need to check this and do bussiness logic to make the reconnections and do this in place.we don;t necessarily need a dummy node.
     --> then we can return the head of our newly connected list.
     
    curr = head 
     
     
    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
            curr = curr.next.next
        else:
            cur.next = curr.next
            curr = curr.next
            
    return head



"""


from sortedcontainers import SortedSet


class Solution:
    # Cleaner implementation of deleteDups
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        if head.next == None:  # Input: 1->>2->3->None
                                # .  Output: 1->2->3
            return head

        curr = head

        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head


#     def deleteDuplicates(self, head: ListNode) -> ListNode:#O(n) time and O(1) space
#         if head == None:
#             return None

#         if head.next == None:
#             return head

#         dummy = ListNode(-1)

#         head2 = dummy


#         ptr1 = head
#         ptr2 = head.next

#         dummy.next = ptr1
#         dummy = dummy.next

#         while ptr1 != None and ptr2 != None:
#             if ptr1.val == ptr2.val:
#                 ptr2 = ptr2.next
#             else:
#                 dummy.next = ptr2
#                 dummy = dummy.next
#                 ptr1 = ptr2
#                 ptr2 = ptr2.next

#         if ptr2 == None:
#             dummy.next = None

#         return head2.next


#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None:
#             return None

#         if head.next == None:
#             return head

#         dummy = ListNode(-1)
#         head2 = dummy
#         container = SortedSet()

#         while head != None:#Input: 1->1->2
#             if head.val not in container:
#                 container.add(head.val)

#             head = head.next


#         for number in container:
#             dummy.next = ListNode(number)
#             dummy = dummy.next


#         return head2.next
