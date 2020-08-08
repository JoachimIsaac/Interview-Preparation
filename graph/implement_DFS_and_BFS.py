"""
Traverse 2D array using BFS and DFS


UMPIRE:
Understand (DFS):
--> When I traverse the 2d array how should i represent the values that I am traversing , should I print them or append them to an array? 
just print them.

--> Can I implement the DFS with the call stack?
yes

--> what if the array is empty? just return False 

--> can we morph our input to utilize a flag variable? yes


BFS:
--> When I traverse the 2d array how should i represent the values that I am traversing , should I print them or append them to an array? 
just print them.

--> what if the array is empty? just return False 
--> can we morph our input to utilize a flag variable? yes

Match DFS:
--> recursion --> base case 
--> order of visiting nodes, down first.abs

Match BFS:
--> queue 
order if visiting nodes 
---> sides first

Plan DFS:
1. check if the array is empty 
2. then create based case where if the postion is valid or we already traversed that spot then we return 
3. if it doesn't trigger, print the current value then change it with the flag, and dfs in or other directions


Plan BFS:
1. check if the array is empty, create a queue and add the first value into it, as a tuples of row col values. POp the current value of the queue into a variable
2. then create based case where if the postion is valid or we already traversed that spot then we (continue) 
3. if it doesn't trigger, print the current value then change it with the flag, and add the next vlaues  in the other directions.


grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
"""

from collections import deque


def BFS(grid):
    if len(grid) == 0:
        return False

    max_row = len(grid)
    max_col = len(grid[0])

    queue = deque([])
    queue.append((0, 0))
    # visited = set()

    while queue:
        cordinates = queue.popleft()
        row = cordinates[0]
        col = cordinates[1]

        if row < 0 or col < 0 or row >= max_row or col >= max_col or grid[row][col] == "#":
            continue

        print(str(grid[row][col]) + " ", end="")
        grid[row][col] = "#"
        queue.append((row, col + 1))
        queue.append((row, col - 1))
        queue.append((row + 1, col))
        queue.append((row - 1, col))

    return grid


def DFS(row, col, grid):

    if len(grid) == 0:
        return False

    max_row = len(grid)
    max_col = len(grid[0])

    if row < 0 or col < 0 or row >= max_row or col >= max_col or grid[row][col] == "#":
        return

    print(str(grid[row][col]) + " ", end="")
    grid[row][col] = "#"

    DFS(row + 1, col, grid)
    DFS(row - 1, col, grid)
    DFS(row, col + 1, grid)
    DFS(row, col - 1, grid)

    return grid


grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# print(BFS(grid))
print(DFS(0, 0, grid))
