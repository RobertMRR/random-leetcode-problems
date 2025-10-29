def isValidPalindrome(s):
    d= ""
    for char in s:
        if char.isalnum():
            d += char.lower()
    print(d)
    print(d[::-1])
    return True if d == d[::-1] else False

print(isValidPalindrome("Was it a car or a cat I saw?"))