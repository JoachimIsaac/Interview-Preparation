"""
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.


Example 1:

Input: 23   
Output: true (23 is a happy number)  
it get's to 1.



Example 2:

Input: 12   
Output: false (12 is not a happy number)  

Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.

UMPIRE:

Understand:
---> what is our input? an integer 
---> can we get the number 1?
---> What does a cycle mean? it goes in a patern hitting the same numbers 
---> Do we have to do this inplace?(can we use extra space?)


Match:
--> fast and slow
--> function which adds tehm up together 
--> hash/set

Plan: 
1. We know that we need to check the sum of the numbers squares
2. what if we create a fuction that does that. It finds the sum of the squares
3. Then we just keep looping until the fast one equal 1 or the fast and slow pointers equal each other. Ofcourse loading a string every time .

def next(self,num):
    str1 = str(num)
    result = 0

    for number in num:
        result += number * number

    return result

def find_happy_number(self,num): 
    if num == 1:
        return True
        
    slow = next(num) 13
    fast = next(next(num))1

    while fast != slow:
        slow = next(slow)
        fast = next(next(fast))
        if fast == 1 or slow == 1:
            return True
        if fast == slow:
            return False

    return False


Interviewer: This gives us the answer but can we do better?

me: Yes we can 

the issue of speed is here because we have to convert the number to a sting to get access to the values to sum and sqaure them . if we can get each consecuetive sum in constant time we can increase the speed of the time complexity to

PLan:

create a helper fuction next that runs in constant time:

what are we really doing? 

23 ===> 13 (how can we get this?)

it is essentially 2 * 2 + 3 * 3 ==> 4 + 9 ==> 13
behind = 23 % 10 = 3
front = 23 // 10  = 2

sum = (front * front) + (behind * behind)

def next(self,num):
    sum = 0
    behind = num % 10
    front = num // 10
    sum = (front * front) + (behind * behind)
    return sum 


O(log(n))time complexity : let's say n is the number of numbers in the path, then we don't have to traverse all the numbers to find out if the number is happy. if fast get's to 1 we ccan return. Also it's the same when it's not a happy number when they meet it doesn't mean we visted all the nodes. and so log(n) fits perfectly for the time comlexity cause fast jumps two numbers each time which is essentially breaking how much we have to traverse

O(1) space , we are only manipulating number values , not storing anything serious


"""


class Solution:
    def find_happy_number(self, num):
        if num == 1:
            return True

        slow = num
        fast = self.next(num)

        # O(kd) time and O(1)space, where n is the number of numbers in the possible sums
        while fast != slow:
            slow = self.next(slow)
            fast = self.next(self.next(fast))

        return slow == 1

    def next(self, num):  # O(1)
        sum = 0

        while num != 0:
            digit = num % 10
            sum += digit * digit
            num = num // 10

        return sum


# class Solution:
#     def find_happy_number(self, num):
#         if num == 1:
#             return True

#         slow = self.next(num)
#         fast = self.next(self.next(num))

#         while fast != slow:  # O(n^2) time and O(1)space
#             slow = self.next(slow)
#             fast = self.next(self.next(fast))
#             if fast == 1 or slow == 1:
#                 return True
#             if fast == slow:
#                 return False

#             return False


#     def next(self, num):
#         # str1 =
#         result = 0

#         for number in str(num):
#             result += int(number) * int(number)

#         return result

s = Solution()
print(s.find_happy_number(23))
print(s.find_happy_number(12))

"""""""
# class Solution:
#     def next(self, n):  # if the number is 1 we will get 1, so it stops at 1
#         sum = 0
#         while n != 0:  # if it hit zero we finish with that number
#             sum += (n % 10) * (n % 10)  # takes the end and adds it to sum
#             n = n // 10  # adds the front to the sum

#         return sum

#     def isHappy(self, n: int) -> bool:
#         turtle = n
#         hare = self.next(n)

#         while turtle != hare:
#             turtle = self.next(turtle)
#             hare = self.next(self.next(hare))
#             if hare == 1:
#                 return True

#         return turtle == 1
