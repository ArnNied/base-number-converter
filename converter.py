from string import digits, ascii_uppercase
from math import floor

chars_list = list(digits + ascii_uppercase)


print(f"Order (ltr): {''.join(chars_list)}")
print("Format: [original_base] [number_to_be_converted] [intended_base]\nEx: 10 2748 16 -> ABC")

while True:
    original_base, submitted_number, intended_base = input("> ").split()

    # SETUP
    original_base = int(original_base)
    intended_base = int(intended_base)
    submitted_number_list = list(submitted_number.upper())

    original_base_chars = chars_list[:original_base]
    intended_base_chars = chars_list[:intended_base]


    # EXCEPTIONS
    if original_base > len(chars_list) or intended_base > len(chars_list):
        raise Exception(f"[original_base] and/or [intended_base] exceed the allowed base ({len(chars_list)})")

    for i in submitted_number_list:
        if i not in original_base_chars:
            raise Exception("[number_to_be_converted] does not follow the [original_base] format")


    # CONVERT THE ORIGINAL NUMBER TO DECIMAL FIRST FOR LIST EASY ACCESS
    calc_decimal = 0
    for i in range(len(submitted_number_list)):
        calc_decimal += original_base_chars.index(submitted_number_list[0 - (i+1)]) * (original_base**i)


    # CALCULATING THE OUTPUT
    output = list()
    while calc_decimal != 0:
        calc_decimal, remainder = divmod(calc_decimal, intended_base)
        output.append(intended_base_chars[remainder])

    # REVERSE THEN JOIN THE LIST TO CREATE A STRING BECAUSE THE PREVIOUS CALCULATION IS DONE IN REVERSE
    output.reverse()
    print(f"{''.join(output)}\n")