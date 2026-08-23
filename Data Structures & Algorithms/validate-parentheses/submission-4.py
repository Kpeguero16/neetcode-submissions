class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        open = []
        close = []
        signMap = {'(': 'open', '{': 'open', '[': 'open', ')': 'close', '}': 'close', ']': 'close'}
        for c in s:
            if signMap[c] == 'open':
                open.append(c)
            else:
                if len(open) == 0: return False
                if c == ')':
                    if open[len(open) - 1] == '(':
                        open.pop()
                    else: return False
                elif c == '}':
                    if open[len(open) - 1] == '{':
                        open.pop()
                    else: return False 
                elif c == ']':
                    if open[len(open) - 1] == '[':
                        open.pop()  
                    else: return False
        return len(open) == 0