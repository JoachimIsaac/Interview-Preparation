"""
Problem Statement #
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


UMPIRE:

Understand: --> What happens if we have an empty array? (return [-1,-1] or we can't get an answer)
            --> Can we get negative numbers? (NO)
            

Match: --> Pointers
       --> Single pass
       --> Time O(n), O(1) space; we would be using no extra space and because it is already sorted we dont have to sort it. 
       

       



Plan: 1. We need to check whether our array has less than or a length of 2 and if it does have that length then we need to actually return [-1,-1]
      2. If we have a valid array we need to set our pointers , one at the start of the array and one at the end.
      3. Then we need to create a while loop that keeps going as long as the start < end , that means that they haven't crossed over each other.
      4. We have to keep comparing the current sum and we need to compare whether it is equal to target.
      5. if it is return the indexes or (start,end), if not based on whether it is greater than or less than  the current target sum we then increment start or decrement end.
      6. we keep looping until the while loop's condition is not satisfied. if not then we return [-1,-1]
"""


class Solution:
    def twoSum(self, arr, target):

        if len(arr) < 2:
            return [-1, -1]

        start = 0
        end = len(arr) - 1

        while start < end:
            start_value, end_value = arr[start], arr[end]
            currentSum = start_value + end_value

            if currentSum == target:
                return [start, end]

            elif currentSum > target:
                end -= 1

            elif currentSum < target:
                start += 1
        return [-1, -1]


solution = Solution()
print(solution.twoSum([1, 2, 3, 4, 6], 6))
print(solution.twoSum([2, 5, 9, 11], 11))
