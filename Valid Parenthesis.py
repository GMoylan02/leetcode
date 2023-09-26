from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = deque()
        for c in s:
            if is_opening(c):
                stack.append(c)
            elif len(stack) == 0 or not matches(stack.pop(), c):
                return False
        if len(stack) > 0:
            return False
        return True


def is_opening(c):
    if c in ('{','[','('):
        return True
    else:
        return False

def matches(a, b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    else:
        return False