def lengthofLastWord(s):
    list_of_s = s.split()
    for string in list_of_s:
        if string is " ":
            list_of_s.remove(list_of_s.index(string))
    print(list_of_s)
    return len(list_of_s[-1])

print(lengthofLastWord("   fly me   to   the moon  "))