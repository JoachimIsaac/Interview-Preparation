"""
(NOT A LEET CODE QUESTION, SIMPLER VERSION OF LEETCODE Kth LARGEST NUMBER)
Problem 2 - Kth frequent number
Find the element that appears k number of times in an array.

Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7

UMPIRE:



Understand: --> Can we get an empty array? (No)
            --> When we get an array does it always have one answer? (yes)
            --> we just need to find the number that appears in the array eight times?
            --


Match: ---> hashtables(likely)
       ---> For loop or while loop
       ---> multiple loops?(likely)


Plan: 

hash = {}

for number in array:
    if number not in hash:
        hash[number] = 1
    else:
        hash[number] += 1

for number in hash:
    if hash[number] == k:
        return number


return False      


Evaluate:
Time ==> O(N + H) Where N is the length of the input array and H is the nubmer of unique values within the input array.

space==> O(H) is the number of unique values in the input array.


"""


class Solution:
    def kthFrequentElement(self, nums, k):
        hash = {}

        for number in nums:
            if number not in hash:
                hash[number] = 1
            else:
                hash[number] += 1

        for number in hash:
            if hash[number] == k:
                return number

        return False


solution = Solution()
print(solution.kthFrequentElement([8, 7, 9, 6, 7, 5, 1], 2))  # output 7
print(solution.kthFrequentElement(
    [6, 8, 7, 9, 7, 6, 7, 5, 8, 5, 8, 5, 8, 1], 4))  # output 8
print(solution.kthFrequentElement(
    [8, 9, 6, 6, 7, 6, 7, 5, 1, 8], 3))  # output 6
