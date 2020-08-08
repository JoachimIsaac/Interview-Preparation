"""
Use this as a reference to pratice getting the hang of DFS

We are just gunna do the depth first search traversal and print each value we visit within the traversal.


This is using an actualy stack so it will be an iterative solution. 


"""


class Solution:

    def DFS(self, grid):

        row_edge = len(grid)

        if row_edge == 0:  # if the grid's empty, return
            return

        col_edge = len(grid[0])

        # Here we have 4 different choices:

        # 1. We could use a set to track the visted (row,col)pairs ad a tuple.

        # 2. We could store the values thems selves into the visited set or we could even flatten the matrix an store the flattened indexes into the set.

        # 3. We could create another grid to track where we have already visted by putting true(or some other indicator in that specific position), we would have to use another matrix so that we do not change our own input.

        # 4. We could change our input each time we visit something and replace it with a flag value, that way we know it is visted, this method takes less space than all the others but you would have to ask for your interviewers permission to morph the input.

        visited = set()

        stack = []

        # We need to start the stack with something to start searching. So this will be our first key value pair.

        # opted to go with tuples, you could actually use strings also , but python hates strings so just for ease of implimentation intially i think it's best
        stack.append((0, 0))

        print("Depth-First Traversal:  ")

        while stack:

            cordinates = stack.pop()

            row = cordinates[0]
            col = cordinates[1]

            # If our current Node is visited or the surrounding positons we have to jump to are invalid. End this iteration of the while loop , start the next iteration(continue).
            if row < 0 or col < 0 or row >= row_edge or col >= col_edge or cordinates in visited:
                continue

            # if none of the cases were triggered, we can add the current node cordinates to our set.

            visited.add(cordinates)

            # let's print out that node right now though.
            print(str(grid[row][col]) + " ", end='')

            # now we have to add the connected nodes to to the stack.
            stack.append((row, col - 1))  # go to the left
            stack.append((row, col + 1))  # go to the right
            stack.append((row - 1, col))  # go up
            stack.append((row + 1, col))  # go down


solution = Solution()

grid = [

    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

solution.DFS(grid)
