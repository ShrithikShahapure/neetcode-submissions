class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

# This is a backtracking solution with stack

# come back to his when you learn backtarcking


        def backtrack(current, open_count, close_count):
            # If the current string is complete, add to result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Try adding '(' if we still have some left
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Try adding ')' if it won't break validity
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        # Start backtracking with empty string
        backtrack("", 0, 0)
        return result