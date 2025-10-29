def encode(strs) -> str:

    singel= "|".join(strs)
    print(singel)
    return singel

def decode(s: str):
    decoded = s.split("|")

    return decoded

print(decode(encode([])))