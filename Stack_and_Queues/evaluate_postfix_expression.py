"""
Understanding:
Assumption - The string will always contain enough numbers to complete the expression
Input: "2 5 - 5 * 3 + "
Output:
-3 5 * 3 +
-15 3 +
-12
Input: "1 + 3 -" Output: 1 3 - -> 1-3 or 3-1?
Do we assume that there is a zero before 1?
e.g3:
Input: "5 6 2  +  4  * *  3  *"
output: 5 8 4 ** 3 *
        5 32 * 3 *
        160 3 *
        480
Input: "5 1 2  +  4  * +  3  -"
Output: 14
The expression is evaluated as follows:
    5 3 4 * + 3 -
    5 12 + 3 -
    17 3 -
    14
Match:
- -> loop to prase through our input
- -> stack to track values and operators
- -> if statements to make operational decisions


Plan:

"5 1 2  +  4  * +  3  -"
if we hit operator pop twice and evaluate
stack = [14]


if "+":
    val2 = stack.pop() 
    val1 = stack.pop()

  result = val1 + val2
  push(result)
if "-":
if "*": ....
return stack[0] or return current_result
Divisoin by zero: Invalid Input?
"""


class Solution:
    def evaluate_postfix_expression(self, s):
        stack = []

        s = s.split()

        for character in s:
            if character.isalnum():
                stack.append(int(character))
            elif character == '+':
                value2 = stack.pop()
                value1 = stack.pop()
                result = value1 + value2
                stack.append(result)
            elif character == '-':
                value2 = stack.pop()
                value1 = stack.pop()
                result = value1 - value2
                stack.append(result)
            elif character == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif character == '/':
                try:  # handles dividing by zero
                    value2 = stack.pop()
                    value1 = stack.pop()
                    result = value1 / value2
                    stack.append(result)
                except ZeroDivisionError:
                    return ('Invalid Input: Cannot Divide by Zero')
        return stack.pop()


solution = Solution()
print(solution.evaluate_postfix_expression("5 1 2  +  4  * +  3  -"))
print(solution.evaluate_postfix_expression("2 5 - 5 * 3 + "))
print(solution.evaluate_postfix_expression("5 6 2  +  4  * *  3  *"))
print(solution.evaluate_postfix_expression("0 0 /  +  4  * *  3  *"))


# Time Complexity: O(n)
# Space Complexity: O(n)
