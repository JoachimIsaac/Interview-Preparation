"""
Convert a 2D array into a 1D array and vice versa


UMPIRE:

Understand 2d to 1d:
--> What is our input and what is our output; 2d array and  we return a 1d array with the values that were in our 2d array
--> What happens if our 2d array is empty? return an empty 1d array 
-->  

Understand 1d to 2d:
--> What is our input and what is our output; 1d array and  we return a 2d array with the values that were in our 1d array
--> What happens if our 1d array is empty? return an empty  array 
-->  do we need to pass in out columns? yes 


Match:
--> arrays and nested arrays 
--> loops 
--> append 
--> formula to figure out what is the rows and cols we need 



plan 2d to 1d:

--> We need to create a 1d array filled with zeros that are equal to n * m where n is the number of rows and m is the number of characters.
--> we need to loop through the 2d array and load the values into the single array, we could use a counter of we could use a formula to flatten it. 
--> after replacing the zeros we can return the 1d array 

time complexity : O(r * c) and space is O(n) where n is the total number of values within the 2d array



plan 1d to 2d:

1. we need to check if the current array is empty or not , if it is return []
2. the we need to figure out how big out 2d array is going to be and what dimensions will it have.
3. we then need to load all the values from the 1d array into the 2d array by using the equation that converts row and col indexes 
4. we need to return the 2d array . 

time O(r * c) and O(r * c) space 
where r is the number of rows and c is the number of cols 


"""


class Solution:
    def flatten_2dArray(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        result = [0 for index in range(rows * cols)]
        counter = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                position = row * cols + col
                result[position] = matrix[row][col]

                # counter += 1

        return result

    def convert_1D_to_2d(self, array, cols):
        if len(array) == 0:
            return -1

        if cols == 0 or len(array) % cols != 0:
            return - 1

        array_length = len(array)
        rows = int(array_length / cols)

        result = [[0 for col in range(cols)] for row in range(rows)]

        for index in range(len(array)):
            curr_row = int(index / cols)
            curr_col = int(index % cols)

            result[curr_row][curr_col] = array[index]

        return result


solution = Solution()

matrix = [

    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(solution.flatten_2dArray(matrix))

# print(solution.flatten_2dArray([]))

# print(solution.flatten_2dArray([[]]))

print(solution.convert_1D_to_2d(array, 4))
print(solution.convert_1D_to_2d([], 4))
print(solution.convert_1D_to_2d(array, 0))
