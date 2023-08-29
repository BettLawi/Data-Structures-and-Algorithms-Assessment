def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return len(stack) == 0

example1 = "([]{})"
example2 = "([)]"
print(is_balanced(example1))  # Output: True
print(is_balanced(example2))  # Output: False
