import re

# Combine first digit and last digit
# Sum all values

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
digits = extract_digits(doc)
print(digits)
numbers = first_last(digits)
print(numbers)
output = sum(numbers)
print(output)
