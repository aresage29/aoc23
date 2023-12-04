from collections import defaultdict

def add_relevant_numbers(schematic):
    total = 0
    gearNumbers = defaultdict(list)

    def is_relevant(x, y):
        # checks if the coordinates are within the schematic and if the value isn't a number or dot
        return (
            0 <= x < len(schematic) and
            0 <= y < len(schematic[x]) and
            schematic[x][y] not in '0123456789.'
        )

    def calculate_GearRatio():
        # Checks for dictionary entries with 2 values and calculates the sum
        # of the first value multiplied by the second value
        sum = 0
        for key in gearNumbers.keys():
            if len(gearNumbers[key]) == 2:
                sum += int(gearNumbers[key][0])*int(gearNumbers[key][1])
        return sum

    def is_GearRatio(x,y,value):
        # Checks if the character at position x,y is a * and then adds the value to the dictionary
        if schematic[x][y] == '*':
            gearNumbers[str(x)+str(y)].append(value)

    # Iterate through the schematic
    for i in range(len(schematic)):
        # Offset is used to skip numbers that have already been added to the total, reseted after each line
        offset = 0
        for j in range(len(schematic[i])):
            # checks if the offset is larger than the length of the line
            if j+offset >= len(schematic[i]):
                offset -=1
                break
            # adds the offset to the current position
            j = j+offset
            # if the offset is larger than 0, the offset is decreased by 1
            if offset > 0:
                offset -= 1
            # checks if the character is a number
            if schematic[i][j].isdigit():
                # Determines the length of the number
                length = 1
                if len(schematic[i]) > j+length+1:
                    while schematic[i][j+length].isdigit():
                        length += 1
                        if len(schematic[i]) == j+length:
                            break
                # Checks if the number is relevant (a character that isn't a number or dot is nearby)
                for field in range((length+2) * 3):
                    # Calculates the coordinates of the field to check
                    y = j + field // 3 - 1
                    x = i + field % 3 - 1
                    # If a char that isn't a number or dot is found, the number is relevant
                    if is_relevant(x, y):
                        # The number is added to the total and the coordinates and value are added to the dictionary
                        # for gear ratios
                        if j+length >= len(schematic[i]):
                            # special case for the last number in a line
                            is_GearRatio(x,y,schematic[i][j::])
                            total += int(schematic[i][j::])
                        else:
                            is_GearRatio(x,y,schematic[i][j: j+length])
                            total += int(schematic[i][j: j+length])
                        offset = length-1
                        break

    return total, calculate_GearRatio()

def read_schematic_from_file(file_path):
    # Read the schematic from the file and return it as a list of lines
    with open(file_path, 'r') as file:
        schematic = [line.strip() for line in file.readlines()]
    return schematic

# Read schematic from data.txt
file_path = 'data.txt'
schematic = read_schematic_from_file(file_path)

# Calculate and print the sum of relevant numbers
result = add_relevant_numbers(schematic)
print(f"Sum of relevant numbers: {result}")

