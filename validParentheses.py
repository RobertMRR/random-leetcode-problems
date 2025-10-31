def isValid(s):
    validator = []
    openings = ["(", "[", "{"]
    for char in s:
        if char in openings:
            validator.append(char)
        else:
            if not validator:
                return False
            elif char == ")":
                if validator[-1] != "(":
                    return False
                else:
                    validator.pop()
            elif char == "]":
                if validator[-1] != "[":
                    return False
                else:
                    validator.pop()
            elif char == "}":
                if validator[-1] != "{":
                    return False
                else:
                    validator.pop()
        
    return not validator

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))
print(isValid("){"))