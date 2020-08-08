"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.


UMPIRE:

-->understand: 
--> we are given an input string and we need to find the first none repeating character in that string.
--> after doing this we need to return the index of that character.
--> can we get an empty string? No
--> what if we get a string of size 1, return 0

match:
--> hash table 
--> array 


Plan: store an array of values in the has table, the number of the character and the index at which we last found it.

then we just need to search through the hash to find the character that is equal to only 1 but the index is the least.

then we need to store that in dex in a variable and return it 


time O(N + k) where N is the length of the string and K is the number of unique characters we have.

space O(K) where k is the number of unique characters we have .
"""


class Solution:
    def firstUniqChar(self, s: str):
        if len(s) == 0:
            return -1

        if len(s) == 1:
            return 0

        container = {}
        unique_char = float("inf")
        """
        s = "leetcode"
        
        {l:[1,0],e:[3,7],t:[1,3],c:[1,4],o:[1,5],d:[1,6]}
        
        
        """
        for index, letter in enumerate(s):

            if letter not in container:
                container[letter] = [1, index]
            else:
                container[letter][0] += 1
                container[letter][1] = index

        for letter in container:
            curr_count = container[letter][0]
            curr_index = container[letter][1]

            if curr_count == 1 and curr_index < unique_char:
                unique_char = curr_index

        if unique_char == float("inf"):
            return -1
        else:
            return unique_char
