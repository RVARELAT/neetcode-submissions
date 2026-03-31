class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) == 1):
            return False

        items = []
        for item in s:
            if item in "([{":
                items.append(item)
            elif item == ')':
                if not items or items[-1] != '(':
                    return False
                items.pop()
            elif item == ']':
                if not items or items[-1] != '[':
                    return False
                items.pop()
            elif item == '}':
                if not items or items[-1] != '{':
                    return False
                items.pop()
            else:
                return False  # not a valid character

        return len(items) == 0
                
