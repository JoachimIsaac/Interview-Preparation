"""
Slight varaition of two sum question.

Problem 1 - Find a pair with given sum
Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.

[3, 2, 6, 9, 5], x = 9 : Returns (3, 6)

[10, 1, 5], x = 7 : Returns null

[], x = 2 : Returns null

[1, 5, 2, 4], x = 6 : Returns (1, 5)


UMPIRE:


Understand(questions): --->Are all the arrays going to be sorted? (NO)
                       --> Can we get an empty array and if we do what do we return ? (yes, return Null)
                       --> Can we just return the answer withing an array?(Yes)
                       --> What if we only have one number? (return NUll)


Match: --> hash table (likely)
       --> loop --> through one pass (likely)


Plan:--> if you don't get a pair return None
    --> get the current difference
     --> ask if the current diffrenece is in the hash, if it is not
     --> add  num as a key and then you can add num  as a value
     --> if the currentSum is in the hash , return [hash[num], current ==> num]

if len(nums) == 0 or len(nums) == 1:
    return None

hash = {}

for num in nums:[3, 2, 6, 9, 5], x = 9
    currentSum = target - num


    if currentSum not in hash:
        hash[num] = num
    else:
        return [hash[num],num]

return None
"""


class Solution:
    def findPairForASum(self, arr, target):

        if len(arr) == 0 or len(arr) == 1:
            return None

        hash = {}

        for num in arr:
            currentSum = target - num

            if currentSum not in hash:
                hash[num] = num
            else:
                return [hash[currentSum], num]

        return None


solution = Solution()
print(solution.findPairForASum([3, 2, 6, 9, 5], 9))
print(solution.findPairForASum([10, 1, 5], 7))
print(solution.findPairForASum([1, 5, 2, 4], 6))
print(solution.findPairForASum([], 2))
