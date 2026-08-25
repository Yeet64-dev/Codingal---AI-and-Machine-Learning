def romantoInt(roman_input):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0
    for char in reversed(roman_input):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    print("The integer value of the Roman numeral", roman_input, "is:", total)
num = (input("Enter a Roman numeral to see it's integer value: "))
romantoInt(num)