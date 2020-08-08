"""

Problem 2 - Validate push/pop sequences of Stack
Given push and pop sequences with distinct values, check if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Example:

Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
Output: True

Following sequence can be performed:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Input: pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
Output: False                  p                    t

s[12]

1 can't be popped before 2.


UMPIRE:

Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
Output: True

Understand:
--> are the values always distinct? yes
--> can we assume that we can have arrays of differing lengths?
--> is there any restrictions to space or time ? No
--> What do we return ? (True or False)


Match:
--> stack to prase sequencing 
--> pointers that track indexes 
--> if statements for the decisions
--> loop to traverse 


Plan:

Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
Output: True


1. We need to keep traversing through pushed and add each number to the stack, until the top of the stack equals the number at the current index of the popped array.
2. When ever the top number on the stack is equal to the current index of popped we pop the number off our stack.
3. after coming out of the loop we check if the stack is empty or not and we return our boolean value



pushed_pointer = 0
popped_pointer = 0
stack = []


while 



pushed = [1, 2, 3, 4, 5],     
          pu

popped = [4, 5, 3, 2, 1]
         po

stack = [1,2,3]



python3  validate_push_pop_sequences_of_stack.py

pushed = [1, 2, 3, 4, 5],     
          pu

popped = [5,4, 3, 2, 1]
         po
true 



[1, 2, 3, 4, 5,6], [5, 4, 3, 2, 1]

"""


class Solution:

    def validate_push_pop_sequences(self, pushed, popped):
        if len(pushed) != len(popped):
            return False

        stack = []

        pop_pointer = 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1

        # print(pop_pointer)
        # print(len(pushed))
        # return pop_pointer == len(pushed)
        return not stack


solution = Solution()

print(solution.validate_push_pop_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(solution.validate_push_pop_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
print(solution.validate_push_pop_sequences([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(solution.validate_push_pop_sequences(
    [1, 2, 3, 4, 5, 6], [5, 4, 3, 2, 1]))
