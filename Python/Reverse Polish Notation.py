class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(tokens)
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x,y: int(x / y)
        }
        stack = deque()
        for i, token in enumerate(tokens):
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](int(x), int(y)))
        return stack.pop()