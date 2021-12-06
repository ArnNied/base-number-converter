import json
from string import ascii_uppercase, digits


class InvalidOriginalBase(Exception):
    pass


class InvalidTargetBase(Exception):
    pass


class IllegalCharacter(Exception):
    pass


class IsNotConverted(Exception):
	pass


class Converter:
    """
    Convert a number from one base to another
    """

    chars_list = digits + ascii_uppercase

    def __init__(
        self, original_number: str, original_base: str, target_base: str
    ) -> None:
        self.original_number = tuple(original_number.upper())
        self.original_base = int(original_base)
        self.target_base = int(target_base)
        self.executed = False

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

        if not (2 <= self.original_base <= len(self.chars_list)):
            raise InvalidOriginalBase(
                f"[original_base] exceed the allowed base (2 - {len(self.chars_list)})"
            )

        if not (2 <= self.target_base <= len(self.chars_list)):
            raise InvalidTargetBase(
                f"[target_base] exceed the allowed base (2 - {len(self.chars_list)})"
            )

    def convert_to_decimal(self) -> None:
        """
        Convert self.original_number to decimal.
        """

        decimal_value = 0
        for i in range(len(self.original_number)):
            current_num = self.original_number[0 - (i + 1)]

            if current_num not in self.original_base_chars:
                raise IllegalCharacter(
                    "[original_number] does not follow the [original_base] format"
                )

            character_value_in_decimal = (
                self.original_base_chars.index(current_num) * self.original_base ** i
            )

            decimal_value += character_value_in_decimal

        return decimal_value

    def calculate_output(self, decimal_value) -> None:
        """
        Calculate desired output.
        """

        calculated_decimal = decimal_value
        while calculated_decimal != 0:
            calculated_decimal, remainder = divmod(calculated_decimal, self.target_base)

            self.output.append(self.target_base_chars[remainder])

    def execute(self) -> str:
        """
        Entry point.
        """

        if not self.executed:
            self.validation()
            self.assign_chars()
            self.calculate_output(self.convert_to_decimal())
            self.output.reverse()
            self.executed = True

        return "".join(self.output)

    def log(self, file_path: str = "./log", force: bool = False):
        """
        Log data to a json file.

        file_path: `str`. Path for the json file.
        force: `bool`. set to `True` to force data to be logged even if it's not converted yet.
        """

        if self.executed or force:
            with open(f"{file_path}.json", "r+") as file:
                data = json.load(file)

                try:
                    index = int(list(data.keys())[-1]) + 1
                except IndexError:
                    index = 1

                data.update(
                    {
                        index: {
                            "original_number": "".join(self.original_number),
                            "original_base": self.original_base,
                            "target_base": self.target_base,
                            "result": "".join(self.output),
                        }
                    }
                )
                file.seek(0)
                json.dump(data, file, indent=2)
        else:
            raise IsNotConverted(
                "Data hasn't been converted, add `force=True` to ignore"
            )