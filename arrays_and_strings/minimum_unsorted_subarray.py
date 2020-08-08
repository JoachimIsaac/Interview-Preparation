"""

Problem #1
We started this problem in class. Now your group will practice the I-R-E steps of UMPIRE: implement a solution for a problem, review and evaluate your code with a few test cases.

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.

Part 2: U-M-P-I-R-E

The goal for this portion is to You might not get to the third problem, and that's okay.



Example 2:
                     r
Input: [1, 3, 2, 0, -1, 7, 10]
        l

plan:
1. we start with the left pointer and traverse until we find a break point, we then break out of the loop. (if curr_number > current_index + 1)we break

2.  we start from the right and traverse the pointer until we find the break point
(if curr_number > current_index + 1) we break 

3.we need to get local min and max. linear scan within the range , sort in varaibles ==> local_min = -1 , local_max = 3

4.  if local_min less than what's behind of left we reduce left , if left != 0 . if local_max greater than the value to the right of RIGHT  increment right. 

Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

time O(n)
space O(1)

######################################################################
Problem #2: Run Length Encoding
Practice all aspects of the UMPIRE technique end-to-end and implement a solution for this problem.

Given an input string, write a function that returns the run-length encoded string for the input string.

For example:

Input: "wwwwaaadexxxxxx"
                 c
                      t
           
           result += string[c] + str(t - c + 1)

hash = {w:4,a:3, d:1,e:1,x:6 }

orderedcontainer   SortedDict()


Output: "w4a3d1e1x6"
Follow up: How would you decode the encoded string into the original string?

UMPIRE:

understand:
--> what if we get an empty string? return ""
--> if we have 1 value we return that value and 1 , "u" --> "u1"
--> Lower case and uppercase ? let's assume all are lowercase 
--> 

"""


class Soulution:
    def find_minimum_unsorted_window(self, arr):
        left = 0
        right = len(arr) - 1
        local_min = float("inf")
        local_max = float("-inf")

        while left < right:
            curr = arr[left]

            if curr > arr[left + 1]:
                break

            left += 1

        if right == left:  # fixed it , due to paulina's tip.
            return 0  # saves us runtime speed

        while right > left:
            curr = arr[right]

            if curr < arr[right - 1]:
                break

            right -= 1

        for index in range(left, right + 1):
            curr = arr[index]

            if curr < local_min:
                local_min = curr

            if curr > local_max:
                local_max = curr

        while left > 0:
            curr = arr[left - 1]

            if curr > local_min:
                left -= 1
            else:
                break

        while right < len(arr) - 1:
            curr = arr[right + 1]

            if curr < local_max:
                right += 1
            else:
                break

        return right - left + 1


arr = [1, 3, 2, 0, -1, 7, 10]
arr1 = [1, 2, 3]
arr2 = [1, 2, 5, 3, 7, 10, 9, 12]
arr3 = [3, 2, 1]
s = Soulution()
print(str(s.find_minimum_unsorted_window(arr)) + " e.g 2 ")
print(str(s.find_minimum_unsorted_window(arr1)) + " e.g 3 ")
print(str(s.find_minimum_unsorted_window(arr2)) + " e.g 1 ")
print(str(s.find_minimum_unsorted_window(arr3)) + " e.g 4 ")
