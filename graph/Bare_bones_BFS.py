"""
Use this as a reference to pratice getting the hang of BFS

We are just gunna do the Breadth first search traversal and print each value we visit within the traversal.


We have to do this with a queue this means we have to do this iteratively. 


"""


from collections import deque


class Solution:

    def BFS(self, grid):

        row_edge = len(grid)

        if row_edge == 0:
            return

        col_edge = len(grid[0])

        queue = deque([])
        visited = set()

        print("BFS Traversal:  ")

        # start with the inital position of (0,0)
        queue.appendleft((0, 0))

        while queue:

            cordinate = queue.popleft()

            row = cordinate[0]
            col = cordinate[1]

            if row < 0 or col < 0 or row >= row_edge or col >= col_edge or cordinate in visited:
                continue

            # add to visited list
            visited.add(cordinate)

            # print current value
            print(str(grid[row][col]) + " ", end='')

            queue.append((row, col-1))  # left
            queue.append((row, col + 1))  # right
            queue.append((row - 1, col))  # up
            queue.append((row + 1, col))  # down


solution = Solution()

grid = [

    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

solution.BFS(grid)
