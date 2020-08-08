"""
Traverse a 2D array row-wise, col-wise, diagonal-wise (both ways)

UMPIRE:

Understand:
--> We need to traverse the 2d array in these 4 ways 
--> What if the 2d array is empty 
--> How do we return out results? Return them in an array 
--> What is our input/function variables? just the 2d matrix we have to traverse.
--> for the diagonals we need to check if the 2d array's rows and columns are equal. 

Match:
--> For loop and append
--> Change up the the row and column pairs to get the correct values for the diagonals,left and right.


Plan:

    diagonal left :[1,6,11,16]
    diagonal right: [4,7,10,13]
    col-wise: [1,5,9,2,6,10,14,3,7,11,15,4,8,12,16]
    row-wise: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

    [
    [1, 2, 3, 4],  ==> (0,0), (1,1) , (2,2), (3,3)  both indexes have to be the same rightward
                        [row][row]
    [5, 6, 7, 8],  ==> (0,3),(1,2),(2,1),(3,0) --> the row is acending each time but the col is decrementing each time  [row][counter]  minus the counter each time we store a value.
    [9, 8, 5, 3],
    [3, 4, 5, 9]
    ]

    [] return 0 


    how do we traverse each row -->  [row][col] ==> for row:
                                                    for col 
    

    how do we traverse each col --> [row][col] ==> for col:
                                                        for row:

    
    how do we traverse the left diagonal --> 
"""


class Solution:
    # O(n^2) time or O(n * m) time and  O(n * m ) space
    # the two values of time are the length of the rows and cols.
    def traverse_matrix_row_wise(self, matrix):
        if len(matrix) == 0:
            return False

        result = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result.append(matrix[row][col])

        return result

    # O(n^2) time or O(n * m) time and  O(n * m ) space
    # the two values of time are the length of the rows and cols.
    def traverse_matrix_col_wise(self, matrix):
        if len(matrix) == 0:
            return False

        result = []

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                result.append(matrix[row][col])

        return result

    # O(n) time and O(n) space/ O(1) space if we don't include the input array.
    # Where n is the number of numbers within the diagonal

    def traverse_matrix_diagonal_wise_left(self, matrix):
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return False

        result = []

        for position in range(len(matrix)):
            result.append(matrix[position][position])

        return result

    # O(n) time and O(n) space/ O(1) space if we don't include the input array.
     # Where n is the number of numbers within the diagonal

    def traverse_matrix_diagonal_wise_right(self, matrix):
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return False

        result = []
        counter = len(matrix[0]) - 1

        for position in range(len(matrix)):
            result.append(matrix[position][counter])
            counter -= 1

        return result


solution = Solution()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


print(str(solution.traverse_matrix_row_wise(matrix)) + " row_wise ")
print(str(solution.traverse_matrix_col_wise(matrix)) + " col_wise ")
print(str(solution.traverse_matrix_diagonal_wise_left(matrix)) + " diagonal_left ")
print(str(solution.traverse_matrix_diagonal_wise_right(matrix)) + " diagonal_right ")
