class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                numStack.append(int(token))
            else:
                second = numStack.pop()
                first = numStack.pop()
                match token:
                    case "+":
                        numStack.append(first + second)
                    case "-":
                        numStack.append(first - second)
                    case "*":
                        numStack.append(first * second)
                    case "/":
                        numStack.append(int(first / second))


        return numStack.pop()