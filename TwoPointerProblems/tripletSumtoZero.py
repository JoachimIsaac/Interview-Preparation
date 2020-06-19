"""
Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

UMPIRE:

Understand: --> can we assume that we can get an array that is empty? (what do we return?) []
            --> what about an array that has two or less values?(return [])
            --> The values always have to be a unique , which mean even though the combination is diffrent, the values specifically have to be different.



Match: --> pointerS (3 OF THEM)
       --> TWO LOOPS
       --> summation


Plan: 
1. we need to check is the input array is less than 3, if it is return an empty array
2. then we need to sort our input array.
3. after sorting it we need to set up a for loop which holds our first pointer and that for loop should end at len(arr) - 2. since we sorted the array we also have to account for the fact that there may be duplicates next to each other, to aviod duplicates all we have to do is use continue to skip the loop if arr[index] == arr[index - 1] when index > 0.
4. we then need to make to pointers that traverse based on what the current total is , these pointers will be updated in a nest while loop. they get initalized within the for loop at left = for_loop_pointer + 1 and right = len(array).
6. whenever we get a sum that is equal to zero we append that into the result array as a sub array of values. 
7 after we go through the entire array we will return the result array. 

if len(arr) < 3:
    return [] 

arr.sort()


for index in range(len(arr)-2):
    left = index + 1
    right = len(arr) - 1 

    

    while left < right:
        val1, val2, val3 = arr[index], arr[left], arr[right]
        currentSum = val1 + val2 + val3
        
        if currentSum == 0:
            result.append([val1,val2,val3])
        elif currentSum > 0:
            right -= 1
        elif currentSum < 0:
            left += 1

return result





Time complexity is O(N^2) go over the time 
Space: O(n), igonoring our result array that is our input , .sort() take up O(n) space because it uses timsort.


"""


class Solution:
    def tripletSumtoZero(self, arr):
        if len(arr) < 3:
            return []

        arr.sort()
        result = []
        print(arr)
        for index in range(len(arr) - 2):
            # skip same element to avoid duplicate triplets
            if index > 0 and arr[index] == arr[index - 1]:
                continue

            left = index + 1
            right = len(arr) - 1

            while left < right:  # [-5, -2,   -1, 2,    3]
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
                elif currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1

        return result


solution = Solution()
# print(solution.tripletSumtoZero([-3, 0, 1, 2, -1, 1, -2, -2]))
# print(solution.tripletSumtoZero([-5, 2, -1, -2, 3]))
print(solution.tripletSumtoZero([-2, 0, 0, 2, 2]))
