"""
LeetCode (Easy)

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

Method to solve: UMPIRE ==> Understand, Match, Implement, Review, Evaluate

Understand:(Questions to the interviewer, things that help clarify the question) 
--> What happens when we have an empty array? one or when both are empty ==> (return and emtpy array)
--> What if there are no intersections found? ==> (return and empty array)
--> Do the order of the results matter? ==> (No)
--> Will the input always be in order?
--> Are we looking to do this in linear time ? (Yes)

Match:(We identify the useful patterns, data structures or algorithms that we can use to solve the problem)
--> We can use a hash set or a set(Very likely)
--> Pointers?(Nuetral, would probably have to sort to make it work)
--> loop thorugh once on a single set of data.

Plan: (How we go about solving the problem, our algorithm)

        1. Create the condition to handle if any of the two arrays are empty.

        2. Turn the first array into a set.

        3. Iterate though the second array and if the current number is in the set
           append the number to our result array. Then remove the number we just added to the results from our set.
        4. Keep doing this until we get through every number in nums2.

        5 return the result array.


        def arr1, arr2 
        
        if len(arr1) == 0 or len(arr2) == 0:
            return []

        
        set1 = set(arr1)
        result = []

        for num in arr2:
            if num in set1:
                result.append(num)

        return result




"""
# Implement the code

"""
Time Complexity: O(N + M) Where N is the length of arr1 and M is the length of arr2.
Space Complexity: O(N + K)  Where N is the length of arr1 and K is the number of unique intersections found.

"""


class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        result = []
        set1 = set(nums1)

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)

        return result


solution = Solution()

# Three examples:
print(solution.intersection([1, 2, 2, 1], [2, 2]))
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(solution.intersection([], [9, 4, 9, 8, 4]))
