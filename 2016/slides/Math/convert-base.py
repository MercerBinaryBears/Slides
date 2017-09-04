import math

def extract_digit(number, base, digit):
    return math.floor(number / (base ** digit)) % base

def number_of_digits(number, base):
    return math.ceil(math.log(number, base))

def convert_to_base(number, base):
    digits = number_of_digits(number, base)
    converted = ''
    for k in range(digits):
        converted = str(extract_digit(number, base, k)) + converted
    return converted

print(convert_to_base(236, 2))
print(bin(236))
