class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element if stack isn't empty, else assign a dummy value
                top_element = stack.pop() if stack else "#"

                # Check if the popped bracket matches the expected open bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0