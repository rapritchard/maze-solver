# Maze Solver
Maze Solver created following the Boot.dev course - BUILD A MAZE SOLVER (Instructions for what to do, not following what to do)

Uses tkinter to render GUI maze.

Uses a recursive depth-first traversal to create the maze and a recursive depth-first search to solve it.

## Running
To run, use the following command:
```shell
python src/main.py
```

## Algorithm to solve
1. Recursive backtracking - The method explores each possible direction (left, right, up and down) to find a path through the maze. It checks each path fully before backtracking.
2. Visited cells - Each cell is marked as visited once explored to avoid revisiting it
3. Base case - The method includes a base case that returns true upon reach the end cell, allowing the recursion to exit and signal success
4. Recursion and undo - The else condition on recursive return uses an undo operation to backtrack, if the path is wrong we reverse the moves and try different directions
