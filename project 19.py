
class RomanConverter:
    """
    A class to convert integers to Roman numerals.
    """

    def __init__(self, value):
        """
        Initialize the RomanConverter with an integer value.
        """
        if not isinstance(value, int) or value <= 0 or value > 3999:
            raise ValueError("Value must be an integer between 1 and 3999.")
        self.value = value

    def to_roman(self):
        """
        """
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        result = ""
        num = self.value

        for key, symbol in roman_numerals.items():
            while num >= key:
                result += symbol
                num -= key

        return result


try:
    converter = RomanConverter(1987)
    print(f"Roman numeral for 1987: {converter.to_roman()}")
except ValueError as e:
    print(e)