class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        stack = []
        open_signs = {'(', '{', '['}
        for c in s:
            if c in open_signs:
                stack.append(c)
            else:
                if len(stack) == 0: return False
                if c == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else: return False
                elif c == '}':
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else: return False 
                elif c == ']':
                    if stack[len(stack) - 1] == '[':
                        stack.pop()  
                    else: return False
        return len(stack) == 0