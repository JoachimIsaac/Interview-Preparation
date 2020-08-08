"""
Problem 1:
Convert a n x m 2D array into a (n * m) x 1 1D array.

Problem 2:
Convert a (n * m) x 1 1D array into a n x m 2D array.



U:

1.what if we get an empty 1d array ?
return [ ]
2. what if we get this [1] ==> [[1]]
3. so if number of cols is invalid , return -1 


M: 
arrays 


plan: 
1. check if empty 
2. check if cols are valid 
3. get values for cols and load the col 
4. return result 

"""


class Solution:
    def convert_2D_to_1D(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        result = [0 for index in range(len(matrix[0]*len(matrix)))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result[row * len(matrix[0]) + col] = matrix[row][col]

        return result

    def convert_1D_to_2D(self, array, cols):
        if len(array) == 0:
            return []

        if cols == 0 or len(array) % cols != 0:
            return -1

        result = [[0 for col in range(cols)]
                  for row in range(int(len(array)/cols))]

        for index in range(len(array)):
            row_index = int(index/cols)
            col_index = index % cols

            result[row_index][col_index] = array[index]

        return result


solution = Solution()
# matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(solution.convert_2D_to_1D(matrix1))
# matrix2 = [[1],[2],[3],[4]]
# print(solution.convert_2D_to_1D(matrix2))
# matrix3 = []
# print(solution.convert_2D_to_1D(matrix3))
# matrix4 = [[]]
# print(solution.convert_2D_to_1D(matrix4))

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(solution.convert_1D_to_2D(array1, 4))
array2 = []
print(solution.convert_1D_to_2D(array2, 0))
array3 = [1, 2, 3]
print(solution.convert_1D_to_2D(array3, 0))
