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
                # check if stack is empty or check if top of stack is a corresponding opening bracket
                if len(bracket_stack) == 0 or bracket_stack[-1] != mapping[bracket]:
                    return False
                bracket_stack.pop()
            else:
                # we have an open bracket
                bracket_stack.append(bracket)
        
        # check if stack is empty 
        return len(bracket_stack) == 0