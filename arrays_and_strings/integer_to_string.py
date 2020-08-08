"""

Problem 2:
Write a method that takes an integer as input and returns its string representation.

For example:

Input: 123
Output: "123"

Input: -6714
Ouput: "-6714"



UMPIRE:

Understand:
--> Can we use the built in str() method to change the entire integer? 
--> Can we get negative numbers ? yes 
--> can we get input that is not an integer? yes


match:
int() method 


Plan:

--> check if the number is an integer, if it is we can continue , if not return "Not an integer value"
--> if it is an integer value return that str representation of that



O(1) constant time 
O(1) constant space 
"""


class Solution:
    def integer_to_string(self, number):
        if isinstance(number, int):
            return str(number)
        else:
            return "Not an integer value"


solution = Solution()

print(solution.integer_to_string(-6714))
