class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their opening counterparts
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map:
                # If stack is empty or top doesn't match, it's invalid
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Return True if all brackets were matched and popped
        return not stack
