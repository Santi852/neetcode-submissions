class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Close = {")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in Close:
                if stack and stack[-1] == Close[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False