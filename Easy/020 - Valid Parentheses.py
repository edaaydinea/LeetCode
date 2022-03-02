class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Traversing the Expression
        for char in s:
            if char in ["(", "{", "["]:
                # push the element in the stack
                stack.append(char)
            else:
                # if current character is not opening bracket, then it must be closing.
                # So stack cannot be empty at this point
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False

        # Check empty stack
        if stack:
            return False
        return True
