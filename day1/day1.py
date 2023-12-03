with open("input.txt", "r") as input_file:
    input_lines = [line.strip() for line in input_file.readlines()]

def find_first_digit(line):
    i = 0
    while not(line[i].isdigit()):
        i+=1
    return line[i]

def sum_of_digits(lines):
    sum = 0
    for line in lines:
        number_str = ''
        number_str += find_first_digit(line)
        number_str += find_first_digit(line[::-1])
        sum += int(number_str)
    return sum

print("Part 1 solution is", sum_of_digits(input_lines))

string_nums = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

updated_input = []
for line in input_lines:
    for key, value in string_nums.items():
        line = line.replace(key, value)
    updated_input.append(line)

print("Part 2 solution is", sum_of_digits(updated_input))