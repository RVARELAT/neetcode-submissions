class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            # push operands onto the stack
            if token not in operators:
                stack.append(token)
            # when we see an operator we pop two operands from the stack,
            # we evaluate that and push the result back to the stack
            elif token in operators:
                first_operand = stack.pop()
                first_operand = int(first_operand)
                second_operand = stack.pop()
                second_operand = int(second_operand)
                if token == '+':
                    result = second_operand + first_operand
                    stack.append(result)
                elif token == '-':
                    result = second_operand - first_operand
                    stack.append(result)
                elif token == '*':
                    result = second_operand * first_operand
                    stack.append(result)
                elif token == '/':
                    # Division in Python / returns float — to truncate toward zero as the problem states, you can replace:
                    result = int(second_operand / first_operand)
                    stack.append(result)

        # once we are done with all tokens in the list, we pop the result from the stack and return
        return int(stack.pop())

# time complecity = O(n) since we traverse the list of tokens once
# space complexity = O(n) since we use a stack for the tokens
        
