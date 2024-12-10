# Start: 9:03pm, End: 10:18pm next day

from collections import Counter

# test_case = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''

# test_case = test_case.split('\n')
# word_search = test_case

file = open('./word_search.txt')
word_search = [line.strip() for line in file.readlines()]
# print(word_search)

neighbors_dict = {
    "RIGHT": [0, 1],
    "BOTTOM_RIGHT": [1, 1],
    "BOTTOM": [1, 0],
    "BOTTOM_LEFT": [1, -1],
    "LEFT": [0, -1],
    "TOP_LEFT": [-1, -1],
    "TOP": [-1, 0],
    "TOP_RIGHT": [-1, 1]
}

word = 'XMAS'
n = len(word)
R, C = len(word_search), len(word_search[0])


# 4 base cases
# 1. out of bounds - return false
# 2. already visited - return false
# 3. not the right letter - return false
# 4. the last character - return true

def dfs(grid, row, col, i, direction, visited):
    if min(row, col) < 0 or row >= R or col >= C:  # catch out of bounds
        return 0
    if (row, col) in visited or grid[row][col] != word[i]:  # catch base case 2 and 3
        return 0

    if i == n - 1:  # we've reached the end
        return 1

    visited.add((row, col))  # keeps track of path
    count = 0

    if direction:  # this makes sure we are looking in the same direction, i. e. M -> A -> S  **1
        nr, nc = neighbors_dict[direction]
        count += dfs(grid, row + nr, col + nc, i + 1, direction, visited)
    else:  # this flow is triggered given that recursion is at 'X' now
        # in the case we find 'M', pass the direction so that it remains the same
        for direct, (dr, dc) in neighbors_dict.items():
            count += dfs(grid, row + dr, col + dc, i + 1, direct, visited)

    return count


# this is the dfs starter, only start dfs from 'X'
total = 0
for r, line in enumerate(word_search):
    for c, char in enumerate(line):
        if char == 'X':
            total += dfs(word_search, r, c, 0, None, set())

print(total)

diagonals = {
    "BOTTOM_RIGHT": [1, 1],
    "BOTTOM_LEFT": [1, -1],
    "TOP_LEFT": [-1, -1],
    "TOP_RIGHT": [-1, 1]
}


def is_xmas(grid, r, c):
    for dr, dc in diagonals.values():
        nr, nc = r + dr, c + dc
        if min(nr, nc) < 0 or nr >= R or nc >= C:
            return 0

    tl, br = diagonals['TOP_LEFT'], diagonals['BOTTOM_RIGHT']
    top_left, bottom_right = grid[r + tl[0]][c + tl[1]], grid[r + br[0]][c + br[1]]

    tr, bl = diagonals['TOP_RIGHT'], diagonals['BOTTOM_LEFT']
    top_right, bottom_left = grid[r + tr[0]][c + tr[1]], grid[r + bl[0]][c + bl[1]]
    # print(r, c, top_left, bottom_left, top_right, bottom_right)

# The condition below may be explained using the visual below:
# The visual also demonstrates why it is unnecessary to search the entire puzzle input
# it is only needed to look for A, and increment our counter when this condition catches one of the cases below.
# 1. M     S    2. M     M      3. S     M      4. S     S
#       A             A               A               A
#    M     S       S     S         S     M         M     M
    if (((top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M'))
            and ((top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M'))):
        return 1

    return 0


total_xmas = 0
# a = 0
for r, line in enumerate(word_search):
    for c, char in enumerate(line):
        if char == 'A':
            total_xmas += is_xmas(word_search, r, c)
            # print(r, c, count)

print(total_xmas)
