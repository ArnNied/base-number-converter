from converter import Converter


print("======================================")
print("\tBASE NUMBER CONVERTER")
print("======================================")

print(f"Ordering (ltr): {Converter.chars_list}")
print("Input: [number_to_be_converted] [original_base] [target_base]")
print("Ex: 2748 10 16 -> ABC ")

while True:
    user_input = input("\n> ").split()

    to_convert, original_base, target_base = user_input

    convert = Converter(
        original_number=to_convert,
        original_base=original_base,
        target_base=target_base,
    )

    result = convert.execute()

    print(result)
