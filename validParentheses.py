def isValid(s):
    validator = []
    openings = ["(", "[", "{"]
    for char in s:
        if char in openings:
            validator.append(char)
        else:
            print(f"validator is: {validator}")
            if validator == []:
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
    return True

#print(isValid("()"))
#print(isValid("()[]{}"))
#print(isValid("(]"))
#print(isValid("([])"))
#print(isValid("([)]"))
print(isValid("){"))