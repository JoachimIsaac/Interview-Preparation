"""
Problem 3:
Reverse the ordering of words in a sentence.

For example:

Input: "The weather is amazing today!"
Output: "today! amazing is weather The"



UMPIRE:

Understand:
--> can we get an empty string? yes
--> can we get a single letter ? yes
--> so we need to reverse the entire sentence but keep the words in the correct order ? yes


match:
--> Two pointer


Plan(with split):
--> we need to split the string into an array so that each word is in an index
--> we then need to reverse all the words
--> and return the joined array

time complexity :O(n) where n is the length of the input string
and space is O(n)


Plan(without split ):
1. we need to check if the string  is empty
2. we need to check if the string is of length 1
3. if the string is not one of  these two lengths we need to split it into an array not ignoring the white spaces, so we could just append all the characters into an array .
4. we need to then reverse the entire thing
6. then we need to traverse this array and get the start and end points of each word, when we get these we reverse them.
7. after reversing all the words and ignoring the white space we need to join the array to a string and return the answer.

time complexity :O(n) where n is the length of the input string
and space is O(n)




"""


class Solution:
    def reordering_words_in_a_sentence1(self, sentence):  # with split
        if len(sentence) == 0:
            return sentence

        if len(sentence) == 1:
            return sentence

        sentence_array = sentence.split(' ')
        self.reverse_array(0, len(sentence_array) - 1, sentence_array)
        return " ".join(sentence_array)

    def reordering_words_in_a_sentence2(self, sentence):
        if len(sentence) == 0:
            return sentence

        if len(sentence) == 1:
            return sentence

        sentence_array = []

        for letter in sentence:
            sentence_array.append(letter)

        self.reverse_array(0, len(sentence_array) - 1, sentence_array)
        print(sentence_array)
        start = 0
        end = 0

        while end < len(sentence_array):

            if sentence_array[end] == " ":
                self.reverse_array(start, end - 1, sentence_array)
                start = end + 1

            if end == len(sentence_array) - 1:
                self.reverse_array(start, end, sentence_array)

            end += 1

        return ''.join(sentence_array)

    def reverse_array(self, start, end, array):

        while start < end:
            array[start], array[end] = array[end], array[start]

            start += 1
            end -= 1


solution = Solution()
print(solution.reordering_words_in_a_sentence1("The weather is amazing today!"))
print(solution.reordering_words_in_a_sentence2("The weather is amazing today!"))
