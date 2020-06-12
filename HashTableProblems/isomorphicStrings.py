"""
205. Isomorphic Strings (Easy)

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

UMPIRE: 

UNDERSTAND: Questions to the interviewer.
            --> I can see that we have to preserve the order of characters, whihc means we are mapping character to character?
            --> Can one character map to two different characters ? (no)
            --> What if one string is empty ? (return false)
            --> What if the strings have differing length? (there will be no strings with differing lengths)
            --> 
            
Match: --> We can use hash tables
       --> We have to use a loop
       --> Do it in one pass with the loop
       

Plan: --> Create two hash tables that stores the key value pairs
      --> A single for loop to traverse both the strings since it is assumed that they have the same lengths.
      --> If the key value pair is not in the hashtable add it, if it already in the hash table compare what the value is to the current value we are trying to add. If it is different return False if not continue.
      --> we keep doing this until the loop stops
      --> after the loop stops return True

Evaluate: --> Time Complexity: O(n) where n is the length of s and t
          --> Space Complexity: O(s) where s is the number of unique letters we have in the varaible s.
 """


# Implementation
class Solution:
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        if len(s) == 0 or len(t) == 0:
            return False

        hash1 = {}
        hash2 = {}

        for index in range(len(s)):

            if s[index] not in hash1:
                hash1[s[index]] = t[index]
            elif hash1[s[index]] != t[index]:
                return False

            if t[index] not in hash2:
                hash2[t[index]] = s[index]
            elif hash2[t[index]] != s[index]:
                return False

        return True


solution = Solution()


print(solution.isIsomorphic("ab", "aa"))
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))
