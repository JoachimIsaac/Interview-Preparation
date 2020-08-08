
"""

733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


UMPIRE:

Understand: 
--> We are given an image which is a 2d array of integers, each integer representing the pixel value of the image (from 0 to 655535) . 
essentially each vlaue within the 2d array stems from values of 0 - 655535
--> We are going to be given a coordinate that tells us where we are starting from.
--> from that coordinate we are going to perform something called flood flood fill, which mean we are going to change all the values of the current pixel to our currenvalue and the value of all other pixels which are connected to that starting pixel and so on . this will be done 4 directionally (assuming that means ==> left, right, up, down), we only change the value is the next pixel is the same as the last.(start_point_value)?
--> we are going to return the modified image as output.
-->the length of the image and image[0] will be in the range [1,50], essentially the length of the outer list will be of range [1,50] and the range of the inner matrix is the same. 
--> the indexing will not be out of bound, for the starting position 
--> 

image = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
        ]

Output: [
        [2,2,2],
        [2,2,0],
        [2,0,1]
        ]
        
        
match:
--> depth first search
--> breadth first search 


plan:
--> check if the array is not empty , return itself right away if it is
--> then we need to create a variable that holds the starting point's value
--> then we need to perform a modified dfs from the starting point
--> from the starting point we change it's value fromwhat ever it is to the new color vlaue 
--> and then we only continue the dfs on values that surrond it that are of the same value.
--> after we return the modified 2d array 




"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if len(image) == 0 or len(image[0]) == 0:
            return image

        visited = set()

        target_color = image[sr][sc]

        self.flood_fill_helper(image, sr, sc, newColor, target_color, visited)

        return image

    def flood_fill_helper(self, image, sr, sc, newColor, target_color, visited):

        max_row = len(image)
        max_col = len(image[0])

        if sr >= max_row or sc >= max_col or sr < 0 or sc < 0 or (sr, sc) in visited or image[sr][sc] != target_color:
            return

        visited.add((sr, sc))
        image[sr][sc] = newColor

        self.flood_fill_helper(image, sr + 1, sc, newColor,
                               target_color, visited)  # down
        self.flood_fill_helper(image, sr, sc + 1, newColor,
                               target_color, visited)  # right
        self.flood_fill_helper(image, sr-1, sc, newColor,
                               target_color, visited)  # up
        self.flood_fill_helper(image, sr, sc-1, newColor,
                               target_color, visited)  # left
