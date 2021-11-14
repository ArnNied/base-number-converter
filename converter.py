from string import digits, ascii_uppercase


class Converter:
    """
    Convert a number from one base to another
    """

    chars_list = digits + ascii_uppercase

    def __init__(
        self, submitted_number: str, original_base: str, target_base: str
    ) -> None:
        self.submitted_number = tuple(submitted_number.upper())
        self.original_base = int(original_base)
        self.target_base = int(target_base)

        self.output = list()

    def assign_chars(self) -> None:
        """
        Assign usable chars for original and intended base.
        """

        self.original_base_chars = self.chars_list[: self.original_base]
        self.target_base_chars = self.chars_list[: self.target_base]

    def validation(self) -> None:
        """
        Check if self.original_base or self.target_base is out of range.
        """

        if self.original_base > len(self.chars_list) or self.original_base < 2:
            raise Exception(
                f"[original_base] exceed the allowed base (2 - {len(self.chars_list)})"
            )

        if self.target_base > len(self.chars_list) or self.target_base < 2:
            raise Exception(
                f"[target_base] exceed the allowed base (2 - {len(self.chars_list)})"
            )

    def convert_to_decimal(self) -> None:
        """
        Convert self.submitted_number to decimal.
        """

        decimal_value = 0
        for i in range(len(self.submitted_number)):
            current_num = self.submitted_number[0 - (i + 1)]

            if current_num not in self.original_base_chars:
                raise ValueError(
                    "[number_to_be_converted] does not follow the [original_base] format"
                )

            original_value_in_decimal = self.original_base_chars.index(current_num)
            intended_value_index = original_value_in_decimal * (self.original_base ** i)

            decimal_value += intended_value_index

        return decimal_value

    def calculate_output(self, decimal_value) -> None:
        """
        Calculate desired output.
        """

        calculated_decimal = decimal_value
        while calculated_decimal != 0:
            calculated_decimal, remainder = divmod(calculated_decimal, self.target_base)
            self.output.append(self.target_base_chars[remainder])

    def reverse_and_join_output(self) -> str:
        """
        Reverse then join the output because the previous calculation is done in reverse.
        """

        self.output.reverse()

        return "".join(self.output)

    def execute(self) -> str:
        """
        Entry point.
        """

        self.validation()
        self.assign_chars()
        self.calculate_output(self.convert_to_decimal())

        return self.reverse_and_join_output()


print(
    """
======================================
		BASE NUMBER CONVERTER
======================================
"""
)
print(f"Ordering (ltr): {Converter.chars_list}")
print("Input: [number_to_be_converted] [original_base] [target_base]")
print("Ex: 2748 10 16 -> ABC ")

while True:
    user_input = input("\n> ").split()

    to_convert, original_base, target_base = user_input

    result = Converter(
        submitted_number=to_convert,
        original_base=original_base,
        target_base=target_base,
    ).execute()

    print(result)
