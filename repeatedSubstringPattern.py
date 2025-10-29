from collections import defaultdict
import re
def repeatedSubstringPattern(s: str) -> bool:
    new= re.split(r"[a-zA-Z]", s)
    print(new)
#set
print(repeatedSubstringPattern("aaa"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
