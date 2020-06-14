"""
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]


UMPIRE:

Understand --> If we get an empty array? (Do we just return and empty array?)




Match --> pointers (likely)
      --> sort (likely)
      --> one pass (likely)



Plan(Naive): 1. Create an if statement to catch an empty array.
             2. Loop through the array and square each number, each time appending the new number to a new array.
             3. sort the array



Plan(Optimal Solution): 1. Check whether our input is empty, if it return an empty array.
                        2. The we need to create a result array that is the same length at the input array, this is going to help us partiant our answer.
                        3. Then we need to create two pointers to traverse our input and a pointer to traverse our result array.
                        4. We will create a left and right pointer for the input array, then when the left pointer's value squared is more than the right pointer's value square, we put that number within the result array via it's current index and then we increment the right counter.
                        5. Any time the left side is less than the right or even equal to we add the right pointer's squared value and then decrement the right pointer.
                        6. This is done until the pointer pass each other (they are no longer <= each other)
                        7. We return our result array.







"""


class Solution:
    def squaringSortedArrayMyNaiveApproach(self, arr):
        # Time O(n * log(n))
        # Space O(n)
        if len(arr) == 0:
            return []

        result = []

        for num in arr:
            result.append(num * num)

        result.sort()

        return result

    def squaringSortedArray(self, arr):
        # Time O(n)
        # Space O(n)
        if len(arr) == 0:
            return []

        n = len(arr)

        result = [0 for _ in range(n)]

        result_index = n - 1
        left = 0
        right = n - 1

        while left <= right:  # [-2, -1, 0,  2,    3]
            leftSquared = arr[left] * arr[left]
            rightSquared = arr[right] * arr[right]

            if leftSquared > rightSquared:
                [0, 1, 4, 4, 9]
                result[result_index] = leftSquared
                left += 1
            else:
                result[result_index] = rightSquared
                right -= 1

            result_index -= 1

        return result


solution = Solution()
print(solution.squaringSortedArrayMyNaiveApproach(
    [-2, -1, 0, 2, 3]))  # [0, 1, 4, 4, 9]


print(solution.squaringSortedArrayMyNaiveApproach(
    [-3, -1, 0, 1, 2]))  # Output: [0 1 1 4 9]


print(solution.squaringSortedArray([-2, -1, 0, 2, 3]))  # [0, 1, 4, 4, 9]


print(solution.squaringSortedArray([-3, -1, 0, 1, 2]))  # Output: [0 1 1 4 9]
