import numpy as np


# Soduko solver from input file or command line

# Usage: python soduko.py <input file>
#        python soduko.py <input string>

# Input file format:
# 9 lines of 9 characters each
# 0 for empty cell
# 1-9 for filled cell

# Input string format:
# 81 characters
# 0 for empty cell
# 1-9 for filled cell

# Output:
# Solved soduko puzzle

# Example:
# python soduko.py 000000000302540000050301070000000004409006005023054790000000050700810000080060009

def solve(puzzle):
    """Solve soduko puzzle"""
    # Find empty cell
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                # Try all numbers
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve(puzzle):
                            return True
                        puzzle[row][col] = 0
                return False
    return True

def is_valid(puzzle, row, col, num):
    """Check if number is valid in cell"""
    # Check row
    for i in range(9):
        if puzzle[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if puzzle[i][col] == num:
            return False
    # Check 3x3 box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[box_row + i][box_col + j] == num:
                return False
    return True

def print_puzzle(puzzle):
    """Print soduko puzzle"""
    print(np.array(puzzle))
    # for row in range(9):
    #     for col in range(9):
    #         print(puzzle[row][col], end='')
    #     print()


def test():
    """Test function"""
    puzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    solve(puzzle)
    print('Puzzle 1')
    print_puzzle(puzzle)
    # assert puzzle == [[1, 4, 7, 8, 9, 5, 2, 6, 3],
    #                   [3, 6, 2, 5, 4, 7, 9, 8, 1],
    #                   [9, 5, 8, 3, 2, 1, 4, 7, 6],
    #                   [8, 9, 5, 7, 1, 3, 6, 2, 4],
    #                   [4, 1, 9, 2, 7, 6, 8, 3, 5],
    #                   [6, 2, 3, 1, 5, 4, 7, 9, 8],
    #                   [2, 7, 6, 9, 3, 8, 1, 5, 4],
    #                   [7, 3, 4, 6, 8, 1, 5, 9, 2],
    #                   [5, 8, 1, 4, 6, 2, 3, 0, 9]]


def main():
    """Main function"""
    import sys
    # Check command line arguments
    if len(sys.argv) != 2:
        print('Usage: python soduko.py <input file>')
        print('       python soduko.py <input string>')
        sys.exit(1)
    # Read input file
    if len(sys.argv[1]) == 81:
        puzzle = []
        for i in range(9):
            puzzle.append([int(sys.argv[1][i * 9 + j]) for j in range(9)])
    else:
        puzzle = []
        with open(sys.argv[1]) as f:
            for line in f:
                puzzle.append([int(c) for c in line.strip()])
    # Solve puzzle
    if solve(puzzle):
        print_puzzle(puzzle)
    else:
        print('No solution')

if __name__ == '__main__':
    # test()
    main()
