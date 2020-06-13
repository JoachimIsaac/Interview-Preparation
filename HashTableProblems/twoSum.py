"""
Two Sum (Easy)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


UMPIRE: 

Understand: --> Can we use one number twice ? (No)
            --> What if we don't find a pair what do we return ? and empty array?(assume thatevery input has atleast one solution)
            --> Should we return the first soulution found ? (yes)
            --> does the order of the indexes matter?
            
MATCH: NESTED LOOPS
       HAS TABLE 
       


Plan: 1. We need to check the sum of each of the numbers and if the sum equal the target sum then we return the indexes.
    

for index len(num) - 1:
    for curr (index + 1 , len(num)):
        current_sum = nums[curr] + nums[index] 
        if current_sum == target:
            return [index, curr]
return []

Evaluate: 
--> time complexity ==> O(n^2)
--> space ==> O(1)


BUT CAN YOU DO BETTER?!

YESSS I CANNNNN!!!

PLAN: 1) Create a hash table to track our value and index (value key pair).
      2) after that we need to ask if the currentSum is in this hash table
         if it is not then we can put the current num in the hash table with it's index as the value.
      3) If the currentSum is in the has table then we return the [hash[currentSum],index]
      if we don't find it we return an empty array.

hash  = {}

for index in range(len(nums)):
    current_sum = target - nums[index]

    if currentSum not in hash:
        hash[nums[index]] = index
    else:
        return [hash[currentSum],index]


Evaluation:
--> Time complexity: O(n) where n is the length of the array.
--> O(n) space 



can we do better !!!?

No, not really


Two pointer approach (could be used for a question that is sorted already, since in this question the input doesn't have to be sorted, this creates a problem. The problem is that we need to solve this in place, if we change the positions of the numbers our output will not always be correct.)

"""


class Solution:
    def twoSum1(self, nums, target):

        if len(nums) == 0:
            return []

        for index in range(len(nums) - 1):
            for curr in range(len(nums)):
                current_sum = nums[curr] + nums[index]
                if current_sum == target:
                    return [index, curr]

        return []

    def twoSum2(self, nums, target):
        if len(nums) == 0:
            return []

        hash = {}

        for index in range(len(nums)):

            current_sum = target - nums[index]
            # print(hash)
            if current_sum not in hash:
                hash[nums[index]] = index
            else:
                return [hash[current_sum], index]

        return []


solution = Solution()

# print(solution.twoSum1([2, 7, 11, 15], 9))
# print(solution.twoSum1([3, 5, 2, -4, 8, 11], 7))
print(solution.twoSum2([2, 7, 11, 15], 9))
print(solution.twoSum2([3, 5, 2, -4, 8, 11], 7))
print("######")
print(solution.twoSum3([2, 7, 11, 15], 9))
print(solution.twoSum3([3, 5, 2, -4, 8, 11], 7))
