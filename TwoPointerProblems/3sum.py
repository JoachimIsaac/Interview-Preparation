"""
15. 3Sum
Medium

6698

795

Add to List

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


UMPIRE:


Understand: --> can we assume that we can get an array that is empty? (what do we return?) []
            --> what about an array that has two or less values?(return [])
            --> The values always have to be a unique , which mean even though the combination is diffrent, the values specifically have to be different

Match: --> pointers
       --> sort
       --> loops


Plan: 1. Create if statement that returns an empty array if the length of the array is less than 3.
      2. Create a for loop that tracks the first number within the 3 sum
      3. Create a statement to ristirc reading duplicate numbers
      4. Create helper fucntion that checks the two sum and adds the triplets which sum up to 0
      5. return the results

"""


class Solution:
    def threeSum(self, nums):

        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for index in range(len(nums) - 2):

            left = index + 1
            right = len(nums) - 1
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            self.twoSumFinder(nums, index, left, right, result)

        return result

    def twoSumFinder(self, arr, index, left, right, result):

        while left < right:

            val1, val2, val3 = arr[index], arr[left], arr[right]
            currentSum = val1 + val2 + val3

            if currentSum == 0:
                result.append([val1, val2, val3])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            elif right > 0:
                right -= 1


solution = Solution()
print(solution.threeSum([-2, 0, 0, 2, 2]))
"""
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""
