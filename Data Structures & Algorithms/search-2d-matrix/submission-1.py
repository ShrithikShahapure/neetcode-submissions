class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If the matrix is empty or the first row is empty → no target possible
        if not matrix or not matrix[0]:
            return False
        
        # Number of rows (m) and columns (n)
        m, n = len(matrix), len(matrix[0])
        
        # We treat the 2D matrix like a flattened sorted array of size m*n
        # Search range is from index 0 to (m*n - 1)
        left, right = 0, m * n - 1
        
        # Standard binary search loop
        while left <= right:
            mid = (left + right) // 2  # middle index in flattened array
            
            # Convert 1D index (mid) back to 2D row/col
            row = mid // n     # integer division → row index
            col = mid % n      # remainder → column index
            mid_value = matrix[row][col]
            
            # Compare with target
            if mid_value == target:
                return True            # found target 🎯
            elif mid_value < target:
                left = mid + 1         # search in the right half
            else:
                right = mid - 1        # search in the left half
        
        # Target not found
        return False


        # Flattened view of the matrix:
        # Index:  0   1   2   3   4   5   6   7   8   9   10  11
        # Value:  1   3   5   7  10  11  16  20  23  30  34  60

            # --- Visual Example ---
            # Suppose mid=5:
            #   row = 5 // 4 = 1
            #   col = 5 % 4 = 1
            # → matrix[1][1] = 11
            #
            # Matrix with mid=5 marked:
            # [
            #   [ 1,  3,  5,  7],
            #   [10, (11), 16, 20],
            #   [23, 30, 34, 60]
            # ]
            # ----------------------