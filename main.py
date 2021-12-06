from converter import (
    Converter,
    IllegalCharacter,
    InvalidOriginalBase,
    InvalidTargetBase,
)


print("======================================")
print("\tBASE NUMBER CONVERTER")
print("======================================")

print(f"Ordering (ltr): {Converter.chars_list}")
print("Input: [number_to_be_converted] [original_base] [target_base]")
print("Ex: 2748 10 16 -> ABC ")

while True:
    user_input = input("\n> ").split()

    try:
        original_number, original_base, target_base = user_input
    except ValueError:
        print("Invalid input")
        continue

    try:
        convert = Converter(
            original_number=original_number,
            original_base=original_base,
            target_base=target_base,
        )
        result = convert.execute()
    except ValueError:
        print("Invalid input")
        continue

    except InvalidOriginalBase:
        print(f"Original base ({convert.original_base}) is out of range (2-36)")
        continue

    except InvalidTargetBase:
        print(f"Target base ({convert.target_base}) is out of range (2-36)")
        continue

    except IllegalCharacter:
        print(
            f"Original number ({''.join(convert.original_number)}) does not follow it's base format ({convert.original_base})"
        )
        continue

    convert.log()

    print(result)
