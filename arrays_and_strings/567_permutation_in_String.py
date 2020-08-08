"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


UMPIRE:
UNDERSTAND: 
--> WE NEED TO  find a sub string within s2 which is a permutation of s1 
--> what happends when s1 is empty? return false 
--> if S1 is a single letter can we just do in ? yes
--> INPUT STRINGS only contain lowercase letters 




MATCH:
--> hash tables 
--> 

Plan: 
--> We need to check if s1 is emtpy ,so we can return 0 
--> if s1 has a length of only 1 then we can check if it is in s2 directly 
--> then we need to generate al the substrings of length s1 and then check if they are a valid permutation of s1, if they are we return True if not we continue. if we never return true we return false 




"""


class Solution:
    def checkInclusion(self, s1: str, s2: str):

        if len(s1) == 0:
            return False

        if len(s1) == 1:
            if s1 in s2:
                return True
            else:
                return False

        start = 0
        s1_container = {}
        s1_container = self.counter_occurrencies(s1_container, s1)

        """                        \
        Input: s1 = "ab" s2 = "eidbaooo"
                                  |
        s1_container = {a:1,b:1}
        s2-container = {a:1,b:1}
        
        """

        for end in range(len(s2)):
            match = False

            if len(s2[start:end + 1]) == len(s1):
                s2_container = {}
                s2_container = self.counter_occurrencies(
                    s2_container, s2[start:end + 1])
                match = self.is_permutation(s1_container, s2_container)

                if match == True:
                    return True

            if len(s2[start:end + 1]) >= len(s1):
                start += 1

        return False

    def is_permutation(self, container1, container2):
        for letter in container1:

            if letter not in container2:
                return False

            if container1[letter] != container2[letter]:
                return False
        return True

    def counter_occurrencies(self, container, string):
        for letter in string:
            if letter not in container:
                container[letter] = 1
            else:
                container[letter] += 1

        return container
