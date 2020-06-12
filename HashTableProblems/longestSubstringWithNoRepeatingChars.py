"""

Longest Substring Without Repeating Characters (Medium)



Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


UMPIRE:

Understand: --> Can we get an empty string? what do we return if we get them? (return 0)
            --> In the case where there is only one letter what do we return ? (reutrn 1)
            --> What if there is multiple of the same letter "aaaa" what do we return? (return 1)
            --> A substring is just a part of the string, but we have to retain the string's order right?


Match: --> We can use a for loop 
       --> A Hash Table 


Plan: --> we need to generate all possible substrings and check if there is all unique chracters in each substring
       --> afterwards we need to check te length of that substring that was generated and we have to keep trackign the max length.


       --> then we return the max length.

        max_length = -inf
        for index(len(str)):
            hash = set()
            for curr(index,len(str)):
                if str[curr] not in hash:
                    hash.add(str[curr])
                    max_length = max(max_length,len(hash))

        return max_length



        evaluate:
        --> time complexity: O(n^2) where n is the length of the string 
        --> space complexity:O(k) where k is the number of non repeating characters.


        Can you do better?
        yes I can 


        Understand: we need try to get this solution running with a time complexity that's linea, i don;t see us doing any better than that due to the nature of the problem. 

        plan :
        --> We need to create a sliding window which slides everytime we keep get a substring that is non repeating, and as soon as it is a repeating substring we need to change(increment) the start of the window and delete whatever value that is in the start of the window.


        evaluate: --> Time complexity O(n) where n is the length of the input string s.
                  --> Space complexity O(k) where k is letters that make up the length of the longest substring with no repeating characters.  
"""


class Solution:
    def lengthOfLongestSubstring1(self, str):

        if len(str) == 0:
            return 0

        max_length = float('-inf')

        for index in range(len(str)):
            hash = set()

            for curr in range(index, len(str)):  # {} legnth = 3

                if str[curr] not in hash:
                    hash.add(str[curr])
                    max_length = max(max_length, len(hash))

                else:
                    hash = set()

        return max_length

    def lengthOfLongestSubstring2(self, str):
        if len(str) == 0:
            return 0

        max_length = float('-inf')
        hash = set()
        start = 0
        end = 0

        while end < len(str):  # "abc a bcbb"
            endVal = str[end]

            if endVal not in hash:  # {b,c} length = 3
                hash.add(endVal)
                max_length = max(max_length, end - start + 1)
                end += 1
            else:
                hash.remove(str[start])
                start += 1

        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring2("abcabcbb"))
print(solution.lengthOfLongestSubstring2("bbbbb"))
print(solution.lengthOfLongestSubstring2("pwwkew"))
