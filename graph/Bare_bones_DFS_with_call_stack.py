"""
Use this as a reference to pratice getting the hang of DFS

We are just gunna do the depth first search traversal and print each value we visit within the traversal.


This is using the call stack, so it will be a recursive solution. 


"""


class Solution:
    def DFS(self, grid):
        row_edge = len(grid)

        if row_edge == 0:  # if the grid's empty, return
            return

        visited = set()

        print("Depth-First Search:  ")

        self.DFSUtil(grid, 0, 0, visited)

    def DFSUtil(self, grid, row, col, visited):

        row_edge = len(grid)
        col_edge = len(grid[0])
        cordinate = (row, col)

        if row < 0 or col < 0 or row >= row_edge or col >= col_edge or cordinate in visited:
            return

        # if none of the cases were triggered, we can add the current node cordinates to our set.
        visited.add(cordinate)

        # print current node
        print(str(grid[row][col]) + " ", end="")

        self.DFSUtil(grid, row + 1, col, visited)  # down
        self.DFSUtil(grid, row - 1, col, visited)  # up
        self.DFSUtil(grid, row, col + 1, visited)  # right
        self.DFSUtil(grid, row, col - 1, visited)  # left


solution = Solution()

grid = [

    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

solution.DFS(grid)
