def strStr(haystack: str, needle: str) -> int:
    # if haystack == needle:
    #     return 0
    # print(len(needle))
    # print(len(haystack))
    # for i in range(len(haystack)-len(needle)+1):
    #     print(i)
    #     print(f"{haystack[i:i+len(needle)]} == {needle}")
    #     if haystack[i:i+len(needle)] == needle:
    #         return i
    
    # return -1
    if needle in haystack:
        return haystack.index(needle[0])
    else:
        return -1
        

#print(strStr(haystack="hello", needle="ll"))
print(strStr(haystack="abcc", needle="c"))