class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(current_s, left, right):
            # Base case: valid combination found
            if len(current_s) == 2 * n:
                res.append(current_s)
                return
            
            # Can we add an opening bracket?
            if left < n:
                backtrack(current_s + "(", left + 1, right)
                
            # Can we add a closing bracket?
            if right < left:
                backtrack(current_s + ")", left, right + 1)
                
        backtrack("", 0, 0)
        return res

        