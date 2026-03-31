class Solution:
    def isValid(self, s: str) -> bool:
        # create dict to easily match up brackets
        mapping = {')':'(',  '}':'{', ']':'['} 
        # initialize stack
        bracket_stack = []
        # loop through string
        for bracket in s:
            # we have a closing bracket
            if bracket in mapping:
                # check if stack is empty 
                if len(bracket_stack) != 0:
                    top = bracket_stack[-1]
                    # check if top of stack is a corresponding opening bracket
                    if top == mapping[bracket]:
                        # pop opening bracket
                        bracket_stack.pop()
                        continue
                    else:
                        return False       
                # no valid openning bracket on stack so return False
                else:
                    return False
            # we have an open bracket
            # I think we just push onto the stack
            bracket_stack.append(bracket)
            
        # check if stack is empty
        if len(bracket_stack) == 0:
            return True
        
        return False