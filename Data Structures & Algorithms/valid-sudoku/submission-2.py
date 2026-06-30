# This is the bitmask solution

# This is not for beginners, but time compelxity is o(1)

# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         rows = [0] * 9
#         columns = [0] * 9
#         boxes = [0] * 9
        
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == '.':
#                     continue
                
#                 num = ord(board[i][j]) - ord('1')  # Convert '1'-'9' to 0-8
#                 mask = 1 << num                    # Create bitmask for the number
#                 box_index = (i // 3) * 3 + (j // 3)
                
#                 # Check if the number is already set in the row, column, or box
#                 if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
#                     return False
                
#                 # Mark the number in the row, column, and box
#                 rows[i] |= mask
#                 columns[j] |= mask
#                 boxes[box_index] |= mask
        
#         return True

# beginner solution

# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         n = 9
#         for i in range(n):
#             for j in range(n):
#                 val = board[i][j]
#                 if val == ".":
#                     continue

#                 # Check the row
#                 for col in range(n):
#                     if col != j and board[i][col] == val:
#                         return False

#                 # Check the column
#                 for row in range(n):
#                     if row != i and board[row][j] == val:
#                         return False

#                 # Check the 3x3 box
#                 box_row_start = (i // 3) * 3
#                 box_col_start = (j // 3) * 3
#                 for r in range(box_row_start, box_row_start + 3):
#                     for c in range(box_col_start, box_col_start + 3):
#                         if (r != i or c != j) and board[r][c] == val:
#                             return False

#         return True

# medium; but o(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 boxes indexed 0–8

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Calculate box index
                box_index = (r // 3) * 3 + (c // 3)

                # If duplicate found
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                # Add value to tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True

