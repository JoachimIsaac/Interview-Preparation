"""
Problem 1:
Write a method reverseWords() that takes a message as an array of characters and reverses the order of the words in place.

Input:
    message =  


      ['c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l']

                     
Output:
"steal pound cake"


UMPIRE:

Understand:
--> What if we get an empty array or an array of length 1 ? --> return the array. ("" )
--> Words will be seperate by spaces 
--> 

Match :
--> pointers 
--> loop 
--> helper method --> reverse 

plan:
1. handle empty and array of length 1 
2. reverse the array of characters
3. loop through array and reverse each word 
4. join and return 


  ['c', 'a', 'k','e', " ", 'a']

                e
   [a," ",e,k,a,c]
          s
  ['c', 'a', 'k','e', " "]



"""


class Solution:
    def reverseWords(self, message):
        if len(message) == 0:
            return ''

        if len(message) == 1:
            return ''.join(message)

        self.reverse(0, len(message)-1, message)

        start = 0

        for end in range(len(message)):
            if message[end] == " ":
                self.reverse(start, end-1, message)
                # if end != len(message)-1:
                start = end + 1
            elif end == len(message) - 1:
                self.reverse(start, end, message)

        return ''.join(message)

    def reverse(self, left, right, message):
        while left < right:
            message[left], message[right] = message[right], message[left]
            left += 1
            right -= 1


solution = Solution()
print(solution.reverseWords(
    ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']))
print(solution.reverseWords([" ", 'c', 'a', 'k', 'e', " "]))
print(solution.reverseWords(['c', 'a', 'k', 'e']))
print(solution.reverseWords(['c', 'a', 'k', 'e', " "]))
