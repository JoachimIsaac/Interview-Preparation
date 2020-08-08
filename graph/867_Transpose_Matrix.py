"""

867. Transpose Matrix


Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000




Input:
[

[1,2,3],
[4,5,6],
[7,8,9]

]


Output: 
[
[1,4,7],
[2,5,8],
[3,6,9]
]


[

[1,2,3],
[4,5,6],
[7,8,9]

]

for row in range(len(result)):
    for col in range(len(result[0])):
        result[row][col] = matrix[col][row] (swap)

[[1,4,7],
 [,,],
 [,,]
]

UMPIRE:

Understand:
--> What input are we going to get ? we are going to get a 2d matrix 
--> Will the rows and cols always be of even length ? no
--> What if the matrix is empty ? we can return the input matrix right away 
--> does it have to be inplace? no 
--> do we have to account for changes in the rows and column lengths ? 

Match:
--> double for loop 
--> look for pattern 


Plan:
1. we can check if the array is empty , if it is return the array 
2. then we need to make a result's matrix where it has the opposite amount of columns and rows 
3. after we need to load it by doing result[row][col] = matrix[col][row] (swap)
4. after that we can return the results matrix.

the result has to be what the for loop is base on or else we will get a index error if the rows and cols are not even 

time complexity O(n * m)
space complexity O(n * m)
"""


class Solution:
    def transpose(self, A: List[List[int]]):

        if len(A) == 0 or len(A[0]) == 0:
            return A

        result = [[0 for row in range(len(A))]for col in range(len(A[0]))]

        for row in range(len(result)):
            for col in range(len(result[0])):
                result[row][col] = A[col][row]

        return result
