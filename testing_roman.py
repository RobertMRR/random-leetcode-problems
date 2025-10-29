def romanToInt(s: str) -> int:
    roman_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    last_char_value = roman_to_int.get(s[:1])
    total = 0
    for char in s[1:]:
        char_value = roman_to_int.get(char)
        temp = 0
        if char_value > last_char_value:
            if last_char_value == roman_to_int.get(s[:1]):
                temp = char_value - last_char_value
            else:
                total += char_value
                print(f"you are inside of a char bigger, char is:{char_value}, last_char_value is: {last_char_value}, temp is: {temp}, total is:{total}")
                continue
        else:
            if last_char_value == roman_to_int.get(s[:1]):
                temp = last_char_value + char_value
                print(f"you are inside of a char smaller, char is:{char_value}, last_char_value is: {last_char_value}, temp is: {temp}, total is:{total}")
            else:
                total += char_value
                print(f"you are inside of a char smaller, char is:{char_value}, last_char_value is: {last_char_value}, temp is: {temp}, total is:{total}")           
                continue
        last_char_value = char_value
        total += temp
    print(total)

#romanToInt("LVIII")
romanToInt("MCMXCIV")