
"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

UMPIRE:

understand:
--> We are given two strings and we need to return true if the  both strings are anagrams of each other. 
--> we can assume that all the letters are lowere case.
--> what if they have unitcode characters? (use hash table for uniqueness)
--> if they are of differing length we can return false 



Match:
--> Hash table 



Plan:
if they are the same size we can load both of these into their own has tables and then compare each of their values. 
if they don't equal each other or the letter doesn't exist we return fasle , if it gets through we return true. 



{a:3,n:1,g:1,r:1,m:1}
{a:3,n:1,g:1,r:1,m:1}


time complexity: O(s + t) where s is the length of the input string s  and t is the length of the input string t 

space complexity: O(u + k) where U is the number of unique values in s and k is the number of unique values in k  

"""


class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}
        """
        {r:0,a:0,t:0}
        {c:0,a:0,r:0}
        return False since t not in s
        
        """

        for letter in s:
            if letter not in hash_s:
                hash_s[letter] = 0
            else:
                hash_s[letter] += 1

        for letter in t:
            if letter not in hash_t:
                hash_t[letter] = 0
            else:
                hash_t[letter] += 1

        for letter in hash_s:
            if letter not in hash_t:
                return False

            if hash_t[letter] != hash_s[letter]:
                return False

        return True
