"""
232. Implement Queue using Stacks


Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


UMPIRE:

--> will pop, peek be called on an empty queue? No
--> does time complexit matter ? 
--> can we utilize deque ?


Match: 
--> Stack multiple
--> condiitonals 
--> 


plan:

1. We need to create two arrays to use as stacks , one for pushing and one for popping 
2. We need to then set up condiitonals to handle when we transfer the values to be popped to the pop stack and when we push the values go from the push stack.
3. We also have to make sure that we don't pop when empty, we don't peek when empty (i.e if popped is empty)
4. is empty should be the case when both are empty or we can leverage a length varaible 


queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false


pushed = [1,2]
popped = []
length = 2

Time complexity is O(1) armotized  and normally O(n) 
space is O(n)
where n is the number if number we are given to work with 

"""


"""
Problem 1:
We are given a stack data structure that supports standard operations like push() and pop(), implement a queue using instances of stack data structure and operations on them.


UMPIRE:

Understand: 
--> Are we restricted to using push and pop , yes 
--> what's fucntions do we support==> enqueue, dequeue, peek , 

Match: 
--> stack 
--> loops 

Plan:

3,4


1,2,



pushed_stack = []

popped_stack = [2]


[] 

Test case:
input:
  q = Queue()
  q.enqueue(3)
  q.enqueue(4)
  print(q.peek())
  print(q.dequeue())
  print(q.dequeue())
  q.enqueue(1)
  q.enqueue(2)
  print(q.dequeue())
  print(q.dequeue())

output:
  3
  3
  4
  1
  2





"""

# enqueue, dequeue, peek


class Solution:

    class Queue:
        def __init__(self):
            self.pushed_stack = []
            self.popped_stack = []
            self.length = 0
            self.front_value = None

        def enqueue(self, value):
            if len(self.pushed_stack) == 0:
                self.front_value = value

            self.pushed_stack.append(value)
            self.length += 1

        def dequeue(self):
            if self.length == 0:
                return
            elif len(self.pushed_stack) != 0 and len(self.popped_stack) == 0:
                while self.pushed_stack:
                    self.popped_stack.append(self.pushed_stack.pop())

            value = self.popped_stack.pop()
            self.length -= 1

            if len(self.popped_stack) != 0:
                self.front_value = self.popped_stack[-1]
            else:
                self.front_value = None

            return value

        def peek(self):
            # if len(self.pushed_stack) == 0 and len(self.popped_stack) == 0:
            #   return

            # elif len(self.pushed_stack) == 0 and len(self.popped_stack) != 0:
            #   return self.popped_stack[-1]

            # elif len(self.pushed_stack) != 0 and len(self.popped_stack) == 0:
            #   return self.front_value
            return self.front_value


q = Solution.Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.peek())
print(q.dequeue())
print(q.dequeue())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# Output:
# 3
# 3
# 4
# 1
# 2

#
