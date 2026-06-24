class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n= len(tokens)
        stack= []
        op = ['+','-','*','/']
        for i in range(n):
            if tokens[i] not in op:
                stack.append(tokens[i])
            else:
                second = int(stack.pop())
                first = int(stack.pop())

                if tokens[i] == "+":
                    stack.append(second + first)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(second * first)
                elif tokens[i] == "/":
                    stack.append(first / second)

        return int(stack[0])
                
        