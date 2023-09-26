# when encountering number, push
# when encounter operator, pop 2, apply operator, push result
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for c in tokens:
            if not is_operator(c):
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operate(num1, num2, c))
        return stack.pop()


def operate(num1: int, num2: int, op: chr):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/' and num2 != 0:
        return int(num1/num2)

def is_operator(c):
    return c == '+' or c == '-' or c == '*' or c == '/'