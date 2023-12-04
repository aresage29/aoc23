import re

def get_first_and_last_digit(input_string):
    # Initialize variables to store the first and last digits
    first_digit = None
    last_digit = None

    # Dictionary mapping English words to their numeric representations
    word_to_digit = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Regex to match the first and last digits
    for key in word_to_digit.keys():
        while re.search(key, input_string) is not None:
            input_string=re.sub(key, key[0]+word_to_digit[key]+key[len(key)-1], input_string)


    for char in input_string:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char

    # Check if the first and last digits are None
    if first_digit is None:
        first_digit = ""
        last_digit = ""
    return int(first_digit + last_digit)

data=[]
file = open("data.txt", "r")
data = file.readlines()
file.close()

sum = 0
for line in data:
    a = get_first_and_last_digit(line)
    sum += a

print(sum)