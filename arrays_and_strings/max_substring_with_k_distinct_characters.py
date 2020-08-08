"""
Problem Statement
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi"


UMPIRE:

Understand:
--> So we need to find the maximum length of a substring with K distinct characters
--> if we get a an empty string or a string of length 1 we could just return 0 or the length of the string 
--> we need to check specifically for the number of distinct characters during the substring and whether they are equal to k 


match:
sliding window 
hash set 





plan(naive): 
1. we need to check for the case of empty string or size of 1 
2. we could get all possible substring within the string and track when ever it has k distinct characters , and store the higher length of the string that fits that criteria each time. 


time complexity : O(n^2) where n is the length of the string
space complexity: O(n)




Plan:

start = 0 
container = {}


max_length = float("inf")

for end in range(len(substring)):
    letter = substring[end]
    

    

    if letter not in container:
        container[letter] = 1
    else:
         container[letter] += 1

    if len(container) >= k:
        while len(container) != k:
            if container[substring[start]] > 1:
                container[substring[start]] -= 1
                start += 1
            elif container[substring[start]] == 1:
                del container[substring[start]]
                start += 1
        
        if len(container) == k:
            max_length = max(max_length,end - start + 1)

    return max_length


we need to move the window every time it exceeds k unique characters 


time complexity: O(n) where n is the length of the string   O(n + n) goes down to O(n)
and the space complexity is O(k) where k is the number of distinct numbers we can have in hash at a time 
        




"""


class Solution:
    def max_substring_k_characters1(self, substring, k):
        if len(substring) == 0:
            return 0

        if len(substring) == 1 and k == 1:
            return 1
        elif len(substring) == 1 and k != 1:
            return 0

        """
                      s
        "a  r  a  a   c  i"
                         e
            max = 4
        """

        max_lenght = float('-inf')
        for start in range(len(substring)):
            length = 0
            for end in range(start, len(substring)):
                length += 1

                if len(set(substring[start:end + 1])) == k:
                    max_lenght = max(max_lenght, length)

        return max_lenght

    def max_substring_k_characters2(self, substring, k):
        if len(substring) == 0:
            return 0

        if len(substring) == 1 and k == 1:
            return 1
        elif len(substring) == 1 and k != 1:
            return 0

        start = 0

        container = {}
        max_length = float("-inf")

        for end in range(len(substring)):
            letter = substring[end]

            if letter not in container:
                container[letter] = 1
            else:
                container[letter] += 1

            # print(substring[start:end + 1])

            while len(container) > k:
                if container[substring[start]] != 1:
                    container[substring[start]] -= 1
                    start += 1
                elif container[substring[start]] == 1:
                    del container[substring[start]]
                    start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


solution = Solution()
# print(solution.max_substring_k_characters1("araaci", 2))
# print(solution.max_substring_k_characters1("araaci", 1))
# print(solution.max_substring_k_characters1("cbbebi", 3))
print(solution.max_substring_k_characters2("araaci", 2))
print(solution.max_substring_k_characters2("araaci", 1))
print(solution.max_substring_k_characters2("cbbebi", 3))
