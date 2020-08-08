"""
Practice all aspects of the UMPIRE technique end-to-end and implement a solution for this problem.

Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.

For example:

Input: [1,2,3]
Output: [1,2,4]

Explanation: 123 + 1 = 124



Input: [5,8,9]
Output: [5,9,0]

Explanation: 589 + 1 = 590


UMPIRE:

Understand:
--> do we just have to increment the number by 1? yes
--> what ifthe number ends with 9 or is 9. we haveto handle cases where 
[1,2,9] , or [9] or [9,9,9] == > [1,0,0,0]
--> we need to store the carry and then add it to the other part
--> Do we have to return an array with the values ? yes 
--> 

Match:
--> pointer/pointers 
--> carry variable 
--> appending to the front if done 


Plan:


 [0,0]
  \
      1  
[1,0,0]


carry = 
replace arr[i] with 0 
increment 
then add the carry to the current Number 
if carry equal false we stop or osmething like that 
if we pass zero and still have a carry, appendleft the the deque


carry = False   if curr_val >= 10: carry = true 



while curr_val
digit = 0 ==> curr_val % 10
curr_val //= 10 


O(n) time and O(n) space where n is the length of the input array
"""

from collections import deque


class Solution:
    def increment_an_abitrary_precsion_integer(self, numbers):
        # handles if the numbers at the start is lower than 9. increments right away.
        if numbers[len(numbers) - 1] < 9:
            numbers[len(numbers) - 1] += 1
            return numbers
        # we need to now handle when it is equal to or greater than 9
        # this means we will have a carry.
        else:
            """

            """
            result = deque([])
            carry = True
            digit = 0
            front = 1

            for index in range(len(numbers)-1, -1, -1):
                if numbers[index] + front >= 10:
                    carry = True
                    digit = (numbers[index] + front) % 10
                    front = (numbers[index] + front) // 10
                    result.appendleft(digit)
                elif numbers[index] + front < 10 and carry:
                    carry = False
                    result.appendleft(numbers[index] + front)
                elif not carry:
                    result.appendleft(numbers[index])

            if carry:
                result.appendleft(front)

        return list(result)


solution = Solution()
print(solution.increment_an_abitrary_precsion_integer(
    [1, 2, 3]), " Example 1 ")
print(solution.increment_an_abitrary_precsion_integer(
    [5, 8, 9]), " Example 2 ")
print(solution.increment_an_abitrary_precsion_integer([9]), " Example 3 ")
print(solution.increment_an_abitrary_precsion_integer(
    [9, 9, 9]), " Example 4 ")
