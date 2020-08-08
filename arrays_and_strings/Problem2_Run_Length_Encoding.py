"""
Problem #2: Run Length Encoding
Practice all aspects of the UMPIRE technique end-to-end and implement a solution for this problem.

Given an input string, write a function that returns the run-length encoded string for the input string.

For example:



eg.1
Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"
Follow up: How would you decode the encoded string into the original string?

e.g2
Input: "w"
Output: "w1"

e.g3
Input: ""
Output: ""

e.g4
Input: "xxxxxx"
Output: "x6"

Understand:
--> Can we get an empty string? yes ==> return ""
--> what if it only has one value? ==> return that value
--> The encoded string is a string filled the letter and followed directly by the number of times it appeared in the original.
--> Are all letters going to be lower case ? yes








Match:
-->hashtable
-->two pointers


Plan(hash_map_based):
1 --> We need to check if the string is empty or if it only has one value
2 --> then we need to create a hash map , with the number of time each letter appears
3 --> we need to loop through our input and create a string by adding the character and the number
   to a results string. when we add it the first time change the value to -1 . we can only add this to the string/arr if the value is not currently -1.
4. join() the array or return the string
5. will we get a multidigit numbers


let's try doing it with 2 pointer

            \
Input: "wwwwaaadexxxxxx"
               \
counter = 3
''
Output: "w4a3d1e1x6"


Plan:
1. we need two pointers
2. the first one let's use know what letter we are looking at and the second one counts the number of repetitions we have of that letter. when the next index is either out of bound or another letter we stop that iteration. each time we increement our coutner variable.
3. we need to add the letter and the number to our result string
4.after the iteration is stopped we set the counter variable back to 0
5. then we return the result string


                      \
Input: "wwwwaaadexxxxxx"
                 \
counter = 5


back = 0
front = 0
result = ""
while front < len(S):
    counter = 0

    while S[front] == S[back]:
        if front < len(S):
            counter += 1
            front += 1


    if S[front] != S[back] or front == len(S) - 1:
        result += S[back] + str(counter)
        back = front



    return result

O(n) time  where n is the length of the input string
O(1) space excluding the output string , if we include the output string we could say O(k + r) where k is the number of unique numbers and r is the total length of the values of each repition.





Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"
                 \\
container = {w:-1,a:-1,d:-1,e:-1,x:-1}




We need to create the decoder as well

decoder:
understand:
--> It should be able to convert a code that has multi digit integers
--> If they are empty or only one value we should handle that also
--> We have to load the character that many times (current_int)

match:
--> loop
--> logic that handles multidigit numbers

           /
w42a3d1e1x66


1. loop through the string and look for an integer
2. if we find an integer we need to add it to the current string , if the index is less than len(S - 1, we can check ahead
   an add that number to the current string

3. if we hit the end we just add that number and stop

4. then we use the list of numbers to create the decoded string

5. and we return that string
"""


class Solution:
    def get_run_length_encoding1(self, S):

        if len(S) == 0:
            return ""

        if len(S) == 1:
            return S + "1"

        container = {}
        result = []
        used = -1

        for letter in S:
            if letter not in container:
                container[letter] = 1
            else:
                container[letter] += 1

        for letter in S:

            if container[letter] != used:

                value = container[letter]

                result.append(letter)
                result.append(str(value))

                container[letter] = used

            else:
                continue

        return ''.join(result)

    def get_run_length_encoding2(self, S):
        if len(S) == 0:
            return ""

        if len(S) == 1:
            return S + "1"

        back = 0
        front = 0
        result = ""

        while front < len(S) - 1:
            counter = 0

            while S[front] == S[back] and front != len(S) - 1:
                if front < len(S):
                    counter += 1
                    if front != len(S) - 1:
                        front += 1

            if S[front] != S[back] or front == len(S) - 1:
                if front != len(S) - 1:
                    result += S[back] + str(counter)
                    back = front
                else:
                    result += S[back] + str(counter + 1)
                    back = front

        return result

    def get_run_length_encoding3(self, S):
        if len(S) == 0:
            return ""

        if len(S) == 1:
            return S + "1"

        result = ""
        index = 0
        while index < len(S):

            counter = 1

            while index < len(S) - 1 and S[index] == S[index + 1]:
                print(S[index], S[index+1])

                counter += 1
                index += 1

            result += S[index] + str(counter)
            index += 1

        return result

    # def decode(self, S):
    #     if len(S) == 0:
    #         return ""

    #     if len(S) == 1:
    #         return S + "1"

    #     decode = ''
    #     count = ''
    #     for char in S:
    #         # If the character is numerical...
    #         if char.isdigit():
    #             count += char
    #         else:
    #             decode += char * int(count)
    #             count = ''

    #     return decode

    def get_letters(self, S, A):
        index = 0
        # curr_number  = ""
        # w42a3d1e1x66

        # [42,3,1,1,66]
        while index < len(S):
            curr_number = ""

            if S[index] not in "0123456789":
                A.append(S[index])

            index += 1


solution = Solution()
string1 = "wwwwaaadexxxxxx"
string2 = "w"
string3 = ""
string4 = "xxxxxx"
print(solution.get_run_length_encoding1(string1))
print(solution.decode(solution.get_run_length_encoding1(string1)))
# print(solution.get_run_length_encoding2(string1))
# print(solution.get_run_length_encoding3(string1))


# print(solution.get_run_length_encoding1(string2))
# print(solution.get_run_length_encoding1(string3))
# print(solution.get_run_length_encoding1(string4))
