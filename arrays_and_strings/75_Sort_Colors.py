"""
75. Sort Colors


Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


UMPIRE:


understand:
--> We are given numbers that represent red, white and blue. that is 0 , 1, and 2
--> will the array ever be empty ? or a length of 1 ? yes if it is empty or a length of 1 return the array


match: 
variables to track count 
double pass 



plan: 
loop through the input array and get the count of the values we have and then overwrite the values in the input array. 



O(n) time 
O(1) space 
in place double pass algorithm 
"""


class Solution:
    def sortColors(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return
        left, right, zero = 0, len(nums)-1, 0

        """
            z    l
        [0,0,1,1,2,2]
               r
        """
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero] = nums[zero], nums[left]
                left += 1
                zero += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1


#     def sortColors(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.


#         Input: [2,0,2,1,1,0]

#         zero = 0
#         one = 0
#         two = 0

#         [0,0,1,1,2,2]
#         """
#         # count sort
#         if len(nums) == 0 or len(nums) == 1:
#             return nums

#         zero = 0
#         one = 0
#         two = 0
#         result = []


#         for number in nums:
#             if number == 0:
#                 zero += 1
#             elif number == 1:
#                 one += 1
#             elif number == 2:
#                 two += 1


#         nums[:zero] = [0] * zero
#         nums[zero:zero + one] = [1] * one
#         nums[zero + one:zero + one + two] = [2] * two
