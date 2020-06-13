"""
128. Longest Consecutive Sequence (leetCode)

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

UMPIRE

Understand: --> Does the squenece have to be contigious? (No)
            --> what if we get an empty array?
            --> if the array is of size 1 (return 1)
            --> what if we get an array of size two? (result could be 2 or 1?)
            --> can you have repeating characters?


Match: --> Hashtable
       --> Counter
       --> Create a counter that jumps each time you check +1 or -1
    
Plan: --> 1. Check if the array is of size 1 or not (check for 1 or 0)
      --> 2. put all the values in  a set so that they are all unique
      --> 3. then we need to traverse the set, our goal should be to find the second lowest number in the streak. in this case it would be two.
      --> 4. then from there we need to check from current - 1 or 1, if it is in the array we add 1 to the currentlongest streak and we keep doing this as long as the current number is within the set. 
      --> we use max to check to longest streak between the current streak and the max streak.


if len(arr) == 0: 
    return 0
elif len(arr) == 1:
    return 1


hash = set(arr)
max_streak = float(inf)

for num in hash:
    

    if num - 1 not in hash:

        currentStreak = 1
        current_num = num

        while current_num + 1 in hash:
            currentStreak += 1
            current_num += 1
        
        max_streak = max(current_streak,max_streak)

    return max_streak

        
    
  

    


"""


# class Solution:
#     def longestConsecutive(self, nums):
#         if len(nums) == 0:
#             return 0
#         elif len(nums) == 1:
#             return 1

#         hash = set(nums)
#         max_streak = float('-inf')

#         for num in hash:
#             if num - 1 not in hash:

#                 current_streak = 1
#                 current_num = num

#             while current_num + 1 in hash:
#                 current_streak += 1
#                 current_num += 1

#             max_streak = max(current_streak, max_streak)

#         return max_streak


class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        hash = set(nums)
        max_streak = float('-inf')

        for num in hash:
            if num + 1 in hash:
                continue

            current_streak = 0

            while num in hash:
                current_streak += 1
                num = num - 1

            max_streak = max(current_streak, max_streak)

        return max_streak


solution = Solution()

print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
