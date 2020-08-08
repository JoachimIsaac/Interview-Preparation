"""
402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


UMPIRE:


Understand:
--> Can the number be negative or have leading zeros? NO
--> we need to remove k digits from the number so that we get the lowest possible number 
--> if the number now leads with a zero we have to make sure there is no zero.
--> if we remove all the digits we have to return "0"


Match:
--> double for loop
--> stack 
--> queue 


Plan:

if k == to the length of the input we return '0'

1. Load all the values in the string inside of the stack in reverse order this will keep the order of the string.
2. if the stack is not empty and the top value of the stack is greater than our current value pop it
3. we can do this k times the poping and we append the rest of the way 
4. after doing this we will have the answer but if all the numbers are equal that means we will just load all of them so we should , have a while loop after this to pop out k numbers if the length of the stack is still equal to the length of the input. 




"112"

1
[1,1]
counter 


"""


class Solution:
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"

        stack = []
        counter = 0

        for number in range(len(num)):

            curr = num[number]

            # while the stack is not empty and the top is >= to the current value and counter != k
            while counter != k and not len(stack) == 0 and stack[-1] > curr:
                stack.pop()
                counter += 1

            stack.append(curr)

        while counter != k:
            stack.pop()
            counter += 1

        return str(int(''.join(stack)))
