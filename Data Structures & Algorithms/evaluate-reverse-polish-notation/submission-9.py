class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integer_stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            # token is an operand
            if token in operators:      
                # pop first element and second element              
                second_num = integer_stack.pop()
                first_num = integer_stack.pop()
                if token == '+':
                    result = first_num + second_num
                    integer_stack.append(result)
                elif token == '-':
                    result = first_num - second_num
                    integer_stack.append(result)
                elif token == '*':
                    result = first_num * second_num
                    integer_stack.append(result)
                elif token == '/':
                    # Because converting the result of normal division to int truncates toward zero.
                    result = int(first_num / second_num)
                    integer_stack.append(result)
                
            # token is an int
            else:
                integer_stack.append(int(token))
        
        return integer_stack[-1]