
I did my 5'th challenge on https://edabit.com/challenge/PzyssSgqopkBjzTY2

-----

Description

Can You Exit the Maze?

Published by: https://edabit.com/user/mNMQvcxKSSvqqMYCH

Key concepts: arrays, functional_programming, games, higher_order_functions

Language: Python


A maze can be represented by a 2D matrix, where 0s represent walkeable areas, and 1s represent walls. You start on the upper left corner and the exit is on the most lower right cell.

Create a function that returns true if you can walk from one end of the maze to the other. You can only move up, down, left and right. You cannot move diagonally.

-----

Examples:

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]) ➞ true

can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]) ➞ false

# This maze only has dead ends!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
]) ➞ false

# Exit only one block away, but unreachable!

can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
]) ➞ true

-----

Notes
- In a maze of size m x n, you enter at [0, 0] and exit at [m-1, n-1].
- There can be dead ends in a maze - one exit path is sufficient.

-----

NOTES TO ME:
- It was faily simple project once you know the trick to solve it, when I was taking my first computer software course I did something similar
- The logis is that think it about like fluid dynamics. The fluid starts at the top left corner, and we are looping through the matrix,
searching for neighbors that have fluid. If they do and if we are a 0 then we make it 5, which is the symbol of having fluid runned.



