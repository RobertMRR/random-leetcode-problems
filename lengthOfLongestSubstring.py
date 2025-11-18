# Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    l, r = 0, 1
    res = 1
    if s == "":
        return 0
    while r < len(s):
        if s[r] in s[l:r]:
            l +=1
        else:
            r += 1
        res = max(res, r-l)
    return res

print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("cdd"))