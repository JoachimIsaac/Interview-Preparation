"""
Remove Duplicates (easy)

Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]




Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

UMPIRE:

Understand: --> Each array that we get will be in order?(yes)
            --> Do we have to use the length the array to get the answe?(Yes, it should be done inplace)
            --> What if we get an array of zero or one ? do we just return the length still? (Yes)

Match: --> pop() or remove()
       --> pointers
       --> trailing pointers
       --> one pass



Plan: 1. We need to do our checks for arrays of length 0 and 1
      2. Afterwards we need to create to pointers, pointer1 and pointer2
      3. Pointer1 is gunna trail behind of pointer2 --> while pointer2 < len(arr)
      4. So we are going to trak each repition by cecking when the values of pointer one and pointer2 equal each other. Everytime they do we increment the counter which keeps tracks of matches.
      5. If they do no match each other we make pointer1 equal pointer 2 and we crement pointer1.
      6. we do this until we break from the while loop, and when we do we return the len(array) - counter(the mathces count).
   
  
   


Evaluate:

   Time: O(N)
   Space: O(1)
"""


class Solution:
    def removeDuplicatesMyWay(self, arr):
        if len(arr) < 2:
            return len(arr)

        pointer1 = 0
        pointer2 = pointer1 + 1

        counter = 0

        while pointer2 < len(arr):

            if arr[pointer1] == arr[pointer2]:  # track all repetitions
                counter += 1
                pointer2 += 1

            else:
                pointer1 = pointer2
                pointer2 += 1

        return len(arr) - counter


"""
Here is the plan for the already done solution:

We are essentially using two points, a leading and a trailing.
Whenever there is a none duplicate found we, place it next to the next none duplicate.
Whenever a none duplicate is found we increment the next_none_duplicate pointer.
The quantity of the point itself dictates the length of the array if all duplicates were eliminated.


Evaluation:
--> Time: O(n)
--> Space: O(1)
"""


def removeDuplicatesSolutionFound(self, arr):
    if len(arr) < 2:
        return len(arr)

    index = 1
    next_none_duplicate = 1

    while index < len(arr):  # [2, 3, 6, 9, 6, 9, 9]

        if arr[next_none_duplicate - 1] != arr[index]:
            arr[next_none_duplicate] = arr[index]
            next_none_duplicate += 1

        index += 1

    return next_none_duplicate


solution = Solution()
print(solution.removeDuplicatesMyWay([2, 3, 3, 3, 6, 9, 9]))
print(solution.removeDuplicatesMyWay([2, 2, 2, 11]))
print(solution.removeDuplicatesSolutionFound([2, 3, 3, 3, 6, 9, 9]))
print(solution.removeDuplicatesSolutionFound([2, 2, 2, 11]))
