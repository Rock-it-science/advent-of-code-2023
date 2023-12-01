import re

# Combine first digit and last digit
# Sum all values

def sub_digit(match: re.Match):
    match = match.group(0)
    if match == 'one': return '1'
    elif match == 'two': return '2'
    elif match == 'three': return '3'
    elif match == 'four': return '4'
    elif match == 'five': return '5'
    elif match == 'six': return '6'
    elif match == 'seven': return '7'
    elif match == 'eight': return '8'
    elif match == 'nine': return '9'

def replace_spelled_numbers(values: list):
    output = []
    for value in values:
        output.append(re.sub(r'one|two|three|four|five|six|seven|eight|nine', sub_digit, value))
        # Likely issue: need to allow overlapping groups
    return output

def extract_digits(values: list):
    output = []
    for value in values:
        output.append(re.findall(r'[0-9]', value))
    return output

def first_last(values: list):
    output = []
    for value in values:
        first = value[0]
        last = value[-1]
        output.append(f'{first}{last}')
    return output

def sum(values: list):
    sum = 0
    for value in values:
        sum += int(value)
    return sum

doc = []
line = None
print('Input calibration document: ')
while line != '':
    line = input()
    doc.append(line)
doc.pop(-1)
repl = replace_spelled_numbers(doc)
print(repl)
digits = extract_digits(repl)
print(digits)
numbers = first_last(digits)
print(numbers)
output = sum(numbers)
print(output)

# 54185 too low